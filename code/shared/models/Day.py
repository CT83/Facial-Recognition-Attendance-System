from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from shared.models.Student import Student
from shared.models.model_setup import Base


class Day(Base):
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Student)
