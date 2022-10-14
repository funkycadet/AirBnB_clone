#!/usr/bin/python3
"""Class BaseModel

This class defines all common attributes/methds for other classes:

- models/base_model.py

- Public instance attributes:
    - id: string - assign with an uuid when an instance is created:
        - uuid.uuid4() can be used to generate unique id
          but must be converted to a string
        - the goal is to have unique id for each BaseModel
    - created_at: datetime - assign with the current datetime
      when an instance is created
    - updated_at: datetime - assign with the current datetime
      when an instance is created and it will be updated every
      time you change your object

- __str__: should print: [<class name>] (<self.id>) <self.__dict__>

- Public instance methods:
    - save(self): updates the public instance attribute updated_at
      with the current datetime
    - to_dict(self): returns a dictionary containing all keys/values
      of __dict__ of the instance:
        - by using self.__dict__, only instance attributes set
          will be returned
        - a key __class__ must be added to this dictionary
          with the class name of the object
        - created_at and updated_at must be converted to string object
          in ISO format:
            format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
            you can use isoformat() of datetime object
        - This method will be the first piece of the serialization
          /deserialization process:
            - create a dictionary representation with “simple object type”
              of our BaseModel

"""
from datetime import datetime
import uuid
# from models import storage


class BaseModel:
    """class BaseModel

    This is the basemodel class for base_model

    """

    def __init__(self, *args, **kwargs):
        """
        Method used to initialize class arguments
        """
        if kwargs is not None and len(kwargs) != 0:
            if '__class__' in kwargs:
                del kwargs['__class__']
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from .__init__ import storage
            storage.new(self)

    def __str__(self):
        """
        String representation when instance is printed
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Save updates to an instance
        """
        self.__dict__.update({'updated_at': datetime.now()})
        from .__init__ import storage
        storage.save()

    def to_dict(self):
        """to_dict method

        Method to return a dictionary with all keys/values of __dict__ of the
        instance

        """
        new_dict = dict(self.__dict__)
        new_dict.update({'__class__': type(self).__name__,
                        'updated_at': self.updated_at.isoformat(),
                         'id': self.id,
                         'created_at': self.created_at.isoformat()})

        return new_dict
