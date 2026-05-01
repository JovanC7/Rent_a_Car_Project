#public -> self.name -- Ova varijablja moze da se pozovi iz te klase ili iz bilo kog drugog meesta
#proteted -> self._name -- Podatak moze da se pozove iz te klase ili klase koje nalsedjuju klasu gde je kreiran
#private -> slef.__name -- moze da se pozova simo iz svoje klase
from Db import Db


class User(Db):

    def __init__(self):
        super.__init__()
        self.__name = ""
        self.__age = 0

        con = super().get_connection()

    def set_name(self,name):
        if len(name) < 1:
            raise ValueError("User name must be at least 1 character")
        else:
            self.__name = name

    def set_age(self,age):
        if age <= 18:
            raise ValueError("User must be at least 18 years old")
        else:
            self.__age = age

    def get_name(self):
            return self.__name

    def get_age(self):
        return self.__age



jovan = User()
jovan.set_name("Jovan")

