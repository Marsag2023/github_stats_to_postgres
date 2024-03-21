# import os
from dotenv import load_dotenv
from config import config
from src.functions import get_repos_stats
from src.postgres_db import PostgresDB

load_dotenv()
# db_config = {
#     'user': os.getenv('POSTGRES_USER'),
#     'password': os.getenv('POSTGRES_PASSWORD'),
#     'host': os.getenv('POSTGRES_HOST'),
#     'port': os.getenv('POSTGRES_PORT'),
#     'dbname': os.getenv('POSTGRES_DB')
#
# db_config = {
#     'user': 'postgres',
#     'password': '****',
#     'host': 'localhost',
#     'port': '5432',
#     'dbname': 'postgres'
# }

params = config()

def main():
    data = get_repos_stats('Marsag2023')
    db = PostgresDB(**params)
    db.insert_data(data)

    for item in db.get_data(5, 'forks'):
        print(item)

    db.export_to_json()


if __name__ == '__main__':
    main()