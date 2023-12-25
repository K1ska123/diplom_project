from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.models import Base
# Устанавливаем соединение с базой данных
USER = "USER"
PASSWORD = "PASSWORD"
BASE_NAME = "MAIN"

DRIVER = 'postgresql+psycopg2'
HOST = 'localhost'
PORT = '5432'

DB_URL = f'{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{BASE_NAME}'
Engine = create_engine(DB_URL)
Session = sessionmaker(Engine)

def first_db_connect():
    while True:
        try:
            Base.metadata.create_all(Engine)
            print(f'Connection to database: Successful')
            break
        except Exception as err:
            print(f'Connection to database: Failed')
            print(err)


if __name__ == '__main__':
    first_db_connect()
    session = Session()
    session.commit()
