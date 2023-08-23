#!/usr/bin/python3
"""
This module defines the User class, representing users in the application.
"""

from models.base_model import BaseModel
from models.base import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    This class defines a User with various attributes.

    Attributes:
        __tablename__ (str): The name of the associated database table.
        email (str): Email of the user.
        password (str): Password of the user.
        first_name (str, optional): First name of the user.
        last_name (str, optional): Last name of the user.
        places (list of Place): List of associated Place instances.
        reviews (list of Review): List of associated Review instances.
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", back_populates="user")
    reviews = relationship("Review", back_populates="user")

    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the User instance.

        Returns:
            str: String representation of the User instance.
        """
        return (
            f"[[User] ({self.id}) "
            f"{{'updated_at': {self.updated_at}, "
            f"'id': '{self.id}', "
            f"'last_name': '{self.last_name}', "
            f"'first_name': '{self.first_name}', "
            f"'email': '{self.email}', "
            f"'created_at': {self.created_at}, "
            f"'password': '{self.password}'}}]"
        )
