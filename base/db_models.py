from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData, String
from sqlalchemy.ext.asyncio import AsyncAttrs


class Model(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }) 


class Share(Model):
    __tablename__ = 'shares'

    id: Mapped[int] = mapped_column(primary_key=True)
    figi: Mapped[str] = mapped_column(String(15))           # FIGI-идентификатор инструмента
    ticker: Mapped[str] = mapped_column(String(10))         # Тикер инструмента
    class_code: Mapped[str] = mapped_column(String(20))     # Класс-код
    lot: Mapped[int]                                        # Лотность
    currency: Mapped[str] = mapped_column(String(5))        # Валюта
    name: Mapped[str] = mapped_column(String(255))          # Название инструмента
    cor: Mapped[str] = mapped_column(String(5))             # Код страны риска
    cor_name: Mapped[str] = mapped_column(String(255))      # Наименование страны риска
    sector: Mapped[str] = mapped_column(String(30))         # Сектор экономики



    def __str__(self):
        return f'Share({self.id}, {self.ticker})'

    def __repr__(self):
        return str(self)
