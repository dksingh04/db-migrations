from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.declarative import declarative_base
#Please set DB URL from env varibales
SQLALCHEMY_DB_URL = "mysql+pymysql://<username>:<password>@127.0.0.1:3306/alembic-db-migration"

engine =  create_engine(SQLALCHEMY_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(metadata=MetaData(schema="alembic-db-migration"))


