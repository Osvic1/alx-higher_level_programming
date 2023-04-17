#!/usr/bin/python3

"""
    This module contains the state class and Base
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """
    Class with id and name attributes of each state
    """

    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True)

    name = Column(
            String(128),
            nullable=False)

    cities = relationship(
            "City",
            backref="state",
            cascade="all, delete")
