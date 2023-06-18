#!/usr/bin/python3
"""Definition of City object
"""

from model_state import Base
from sqlalchemy import String, Column, Integer, ForeignKey


class City(Base):
    """City class"""

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
