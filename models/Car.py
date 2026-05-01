# Automobil moze biti samo audi, bmw , mercedes
# Modelli : Audi: A4,A5,A6
# BMW: M3, M5
# Mercedes : GLK , GLE

# Bonus: stavi da svaki model ima svoju godinu proizvodnje, zadatak je da napravimo
#attribut production year
# Ako stavimo Audi A4 -> korisnik moze da getuje vrednost, ali ne moze da upise


class Car:
    VALID_CARS = {
        "AUDI": [
            {"model": "A4", "production_year": 2004},
            {"model": "A5", "production_year": 2003},
            {"model": "A6", "production_year": 2002},
        ],
        "BMW": [
            {"model": "M5", "production_year": 2010},
            {"model": "M3", "production_year": 2008},
        ],
        "MERCEDES": [
            {"model": "GLK", "production_year": 2015},
            {"model": "GLE", "production_year": 2017},
        ],
    }

    def __init__(self):
        self.__brand = None
        self.__model = None


    @property # get dekorator
    def model(self):
        if self.__model is None:
            return f"Model not entered yet."
        else:
            return f"Model: {self.__model}"

    @property # get dekorator
    def brand(self):
        if self.__brand is None:
            return f"Brand not entered yet."

        else:
            return f"Brand: {self.__brand}"

    @property
    def production_year(self):
        if self.__brand is None or self.__model is None:
            return f"Enter a brand or model!"

        for car in Car.VALID_CARS[self.__brand]:
            if car['model'] == self.__model:
                return f"Production year of this car is {car["production_year"]}"




    @brand.setter # SETTER ZA BRAND
    def brand(self,brand):
        brand = brand.upper()
        if not isinstance(brand, str) :
            raise ValueError("Brand not entered yet.")
        else:
            if brand in Car.VALID_CARS.keys():
                self.__brand = brand
            else:
                raise ValueError("The brand must be audi, bmw or mercedes!")


    @model.setter # SETTER MODEL
    def model(self, model):
        model = model.upper()
        valid_models = []
        for car in Car.VALID_CARS[self.__brand]:
            valid_models.append(car["model"])

        if model in valid_models:
                self.__model = model
        else:
                raise ValueError(f"Not valid model! Allowed models are {valid_models}")




#### DEMO ###
car1 = Car()
print(car1.brand)
print(car1.model)

car1.brand = "Mercedes"
print(car1.brand)

car1.model = "GLE"
print(car1.model)
print(car1.production_year)






