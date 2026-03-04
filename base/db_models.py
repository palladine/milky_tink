from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncAttrs


class Model(AsyncAttrs, DeclarativeBase):
    __abstract__ = True



class Share(Model):
    __tablename__ = 'shares'

    id: Mapped[int] = mapped_column(primary_key=True)
    figi: Mapped[str] = mapped_column(String(15))           # FIGI-идентификатор инструмента
    ticker: Mapped[str] = mapped_column(String(6))          # Тикер инструмента
    class_code: Mapped[str] = mapped_column(String(10))     # Класс-код
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
