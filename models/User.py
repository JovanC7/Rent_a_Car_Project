from Db import Db


class User(Db):

    def __init__(self):
        super().__init__()
        self.__name = None
        self.__age = None

        con = super().get_connection()

    # GET METHODS

    @property
    def name(self):
        if self.__name is None:
            raise ValueError("User name must be set")

        else:
            return self.__name

    @property
    def age(self):
        if self.__age is None:
            raise ValueError("User age must be set")
        else:
            return self.__age

    # SET METHODS

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("User name must be of type str")
        elif len(name) < 1:
            raise ValueError("User name must be at least 1 character")
        else:
            self.__name = name

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError("Age must be of type int")
        elif age <= 18:
            raise ValueError("User must be at least 18 years old")
        else:
            self.__age = age



