#!/usr/bin/python3
"""Place Module for HBNB project."""
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from os import getenv


class Place(BaseModel, Base):
    """A place to stay."""
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60), ForeignKey('places.id'),
                                     primary_key=True, nullable=False),
                              Column('amenity_id', String(60), ForeignKey('amenities.id'),
                                     primary_key=True, nullable=False))
        amenities = relationship('Amenity', secondary=place_amenity, back_populates='place_amenities')

    else:
        @property
        def amenities(self):
            """Getter method for amenities."""
            amenity_list = []
            for amenity_id in self.amenity_ids:
                key = 'Amenity.' + amenity_id
                if key in FileStorage.__objects:
                    amenity_list.append(FileStorage.__objects[key])
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """Setter method for amenities."""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)


    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

