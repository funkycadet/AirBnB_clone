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
from datetime import date, datetime
from uuid import uuid4
# from models import storage


class BaseModel:
    """class BaseModel

    This is the basemodel class for base_model

    """

    def __init__(self, *args, **kwargs):
        """__init__ class

        Method used to initialize class arguments

        """
        if not kwargs:
          self.id = str(uuid4())
          self.created_at = datetime.now
          self.updated_at = self.created_at
        else:
          f = "%Y-%m-%dT%H:%M:%S.%f"
          for key, value in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
              value = datetime.strptime(kwargs[key], f)
            if key != '__class__':
              setattr(self, key, value)

    def __str__(self):
      """__str__ method

      Method to print object instance of BaseModel class

      """
      class_name = "[" + self.__class__.name__ + "]"
      dct = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
      return class_name + " (" + self.id + ") " + str(dct)

    def save(self):
      """save method

      Method to update last updated time

      """
      self.updated_at = datetime.now
      # storage.save()

    def to_dict(self):
      """to_dict method

      Method to return a dictionary with all keys/values of __dict__ of the
      instance

      """
      new_dict = {}

      for key, values in self.__dict__.items():
        if key == "created_at" or key == "updated_at":
          new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
        else:
          if not values:
            pass
          else:
            new_dict[key] = values
      new_dict['__class__'] = self.__class__.__name__

      return new_dict
