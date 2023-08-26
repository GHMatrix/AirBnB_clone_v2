#!/usr/bin/python3
"""Amenity Module for HBNB project."""
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Amenity class."""
    __tablename__ = 'amenities'  # Table name

    name = Column(String(128), nullable=False)  # Column for amenity name

    # Relationship with Place using a Many-to-Many relationship
    place_amenities = Table(
        'place_amenity',
        Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
               primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
               primary_key=True, nullable=False)
    )

    places = relationship("Place", secondary=place_amenities, back_populates="amenities")
