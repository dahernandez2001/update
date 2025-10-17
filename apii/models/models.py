import os
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class pelicula(Base):
    __tablename__ = "pelicula"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    directores = relationship("autor", back_populates="pelicula")

class directores(Base):
    __tablename__ = "direcotores"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    pelicula_id = Column(Integer, ForeignKey("pelicula_id"))
    pelicula = relationship("pelicula", back_populates="directores")