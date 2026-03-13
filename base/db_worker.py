from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import select, delete
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import selectinload


def connect(func):
    async def wrapper(self, *args, **kwargs):
        async with self.async_fabric() as session:
            try:
                return await func(self, *args, session=session, **kwargs)
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.close()
    return wrapper



class FilterParser:
    OPERATORS = {
        'gt': lambda f, v: f > v,
        'lt': lambda f, v: f < v,
        'gte': lambda f, v: f >= v,
        'lte': lambda f, v: f <= v,
        'eq': lambda f, v: f == v,
        'ne': lambda f, v: f != v,
        'like': lambda f, v: f.like(v),
        'ilike': lambda f, v: f.ilike(v),
        'startswith': lambda f, v: f.startswith(v),
        'endswith': lambda f, v: f.endswith(v),
        'contains': lambda f, v: f.contains(v),
        'in': lambda f, v: f.in_(v if isinstance(v, list) else [v]),
        'not_in': lambda f, v: f.not_in(v if isinstance(v, list) else [v]),
        'is_null': lambda f, v: f.is_(None) if v else f.isnot(None),
    }
    
    @classmethod
    def parse(cls, model, filters: dict):
        conditions = []
        
        for key, value in filters.items():
            if '__' in key:
                field_name, op_name = key.split('__', 1)
                if hasattr(model, field_name) and op_name in cls.OPERATORS:
                    field = getattr(model, field_name)
                    op_func = cls.OPERATORS[op_name]
                    conditions.append(op_func(field, value))
            else:
                # Простое равенство если нет оператора
                if hasattr(model, key):
                    conditions.append(getattr(model, key) == value)
        
        return conditions





class DBWorker:
    def __init__(self, db_user, db_pass, db_host, db_port, db_name):
        self.url = f'postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
        self.engine = create_async_engine(self.url)
        self.async_fabric = async_sessionmaker(self.engine, expire_on_commit=False)


    @connect
    async def _get_one(self, model, session=None, filters=None):
        if session:
            if not filters:
                filters = {}

            mapper = inspect(model)
            relats = mapper.relationships
            stmt = select(model).filter_by(**filters)

            for relat in relats:
                relat_attr = getattr(model, relat.key)
                stmt = stmt.options(selectinload(relat_attr))

            result = await session.execute(stmt)
            return result.scalar_one_or_none()
        

    @connect
    async def _get(self, model, session=None, filters=None):
        if session:
            if not filters:
                filters = {}
            
            mapper = inspect(model)
            relats = mapper.relationships
            _filters: list = FilterParser.parse(model, filters)
            stmt = select(model).filter(*_filters)

            for relat in relats:
                relat_attr = getattr(model, relat.key)
                stmt = stmt.options(selectinload(relat_attr))

            result = await session.execute(stmt)
            return result.scalars().all()


    @connect
    async def _add(self, items=None, session=None):
        if items and session:
            session.add_all(items)
            await session.commit()


    @connect
    async def _delete(self, model, session=None, filters=None):
        if session:
            if not filters:
                filters = {}
            _filters: list = FilterParser.parse(model, filters)
            stmt = delete(model).filter(*_filters)
            result = await session.execute(stmt)
            await session.commit()
            return result.rowcount
