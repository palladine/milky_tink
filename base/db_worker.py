from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import select


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





class DBWorker:
    def __init__(self, db_user, db_pass, db_host, db_port, db_name):
        self.url = f'postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
        self.engine = create_async_engine(self.url)
        self.async_fabric = async_sessionmaker(self.engine, expire_on_commit=False)


    @connect
    async def _get_one(self, model, session=None, **filters):
        stmt = select(model).filter_by(**filters)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()
        

    @connect
    async def _get_all(self, model, session=None, **filters):
        
        return f'We are in "_get" method DBWorker with "{model}"!'


    @connect
    async def _add(self, model, items=None, session=None):
        if items and session:
            session.add_all(items)
            await session.commit()
        return f'We are in "_add" method DBWorker with "{model}"!'