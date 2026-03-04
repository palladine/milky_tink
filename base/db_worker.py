import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class DBWorker:
    def __init__(self):
        self.url = f'postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}'
        self.engine = None


    def get_connection(self):
        self.engine = create_async_engine(self.url)
        self.async_session_maker = async_sessionmaker(self.engine, expire_on_commit=False)

