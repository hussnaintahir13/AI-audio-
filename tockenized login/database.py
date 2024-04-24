from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL= 'postgresql://postgres:hussnaintahir13@localhost:5432/projectdata'
engine=create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal =sessionmaker(bind=engine,expire_on_commit=False)