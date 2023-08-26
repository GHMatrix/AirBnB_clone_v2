#!/usr/bin/python3
"""
Place Module for HBNB project
"""

from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, backref


class Place(BaseModel, Base):
    """
    A place to stay
    """
    __tablename__ = 'places'

    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        
        reviews = relationship('Review', backref='place', cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary='place_amenity', viewonly=False, backref='place_amenities')

    else:
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

        @property
        def reviews(self):
            """
            Returns list of review instances with place_id
            equals to the current Place.id
            FileStorage relationship between Place and Review
            """
            from models import storage
            all_revs = storage.all(Review)
            return [rev for rev in all_revs.values() if rev.place_id == self.id]

        @property
        def amenities(self):
            """
            Returns the list of Amenity instances based on the
            attribute amenity_ids that contains all Amenity.id
            linked to the Place
            """
            from models import storage
            all_amens = storage.all(Amenity)
            return [amen for amen in all_amens.values() if amen.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """
            Method for adding an Amenity.id to the attribute amenity_ids.
            Accepts only Amenity objects
            """
            if obj is not None and isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
