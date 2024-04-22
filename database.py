import sqlalchemy


DATABASE_URL= 'postgresql://username:hussnaintahir13@host/postgres'
engine=sqlalchemy.create_engine(DATABASE_URL)
Base=sqlalchemy.declarative_base
SessionLocal =sqlalchemy.sessionmaker(bind=engine,expire_on_commit=False)