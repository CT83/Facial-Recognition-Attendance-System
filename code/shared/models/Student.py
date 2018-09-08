from sqlalchemy import Column, Integer, String

from shared.models.model_setup import Base


class Student(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    face_id = Column(String(250), nullable=True)
