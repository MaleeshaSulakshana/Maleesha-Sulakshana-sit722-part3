from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://admin:auRhtYaf08rO0fupnIIKw8MaRycpPetg@dpg-cs3773u8ii6s738hj1bg-a.oregon-postgres.render.com/sit722_part3_v3lh" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
