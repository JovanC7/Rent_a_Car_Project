# from Db import Db


class User():
    users = []

    def __init__(self):
        #  super().__init__()
        self.__name = None
        self.__age = None

    def __str__(self):
        return f"{self.__name} {self.__age}"

    def __repr__(self):
        return self.__str__()

    # con = super().get_connection()

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
    def name(self, Newname):
        if not isinstance(Newname, str):
            raise ValueError("User name must be of type str")
        elif len(Newname) < 1:
            raise ValueError("User name must be at least 1 character")
        else:
            split_name = Newname.split()
            if len(split_name) < 2:
                raise ValueError("Name format must bi 'first name last name'")
            else:
                self.__name = Newname

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError("Age must be of type int")
        elif age <= 18:
            raise ValueError("User must be at least 18 years old")
        else:
            self.__age = age

    def create(self):
        if self.__name is None or self.__age is None:
            raise ValueError("Name or age are not set")
        else:
            print("User created successfully")
            User.users.append(self)
