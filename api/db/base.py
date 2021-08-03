import databases
import sqlalchemy


from .settings import settings

url_database = (
                'postgresql://'
                f'{settings.postgres_user}:'
                f'{settings.postgres_password}'
                '@databaseb:5432/'
                f'{settings.postgres_db}'
                )
database = databases.Database(url_database)
engine = sqlalchemy.create_engine(url_database)
metadata = sqlalchemy.MetaData()
