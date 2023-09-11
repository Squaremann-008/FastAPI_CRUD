from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://oiseh:5PNWs2xgyVCJza0P3lr1wsQkDN4xwWBN@dpg-cjvelut175es73fvt0v0-a.oregon-postgres.render.com/stage2db"  # PostgreSQL database file

Base = declarative_base()

class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    age = Column(Integer)

engine = create_engine(DATABASE_URL)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

