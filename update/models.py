from sqlalchemy import Column, Integer, String

from database import Base

class Mahasiswa(Base):
    __tablename__ = "mahasiswa"

    npm = Column(String, primary_key=True, index=True)
    nama = Column(String)

