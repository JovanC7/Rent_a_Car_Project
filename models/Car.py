class Car:
    VALID_CARS = {
        "AUDI": [
            {"model": "A4", "production_year": 2004, "rented": False, "rented until": None},
            {"model": "A5", "production_year": 2003, "rented": True, "rented until": None},
            {"model": "A6", "production_year": 2002, "rented": False, "rented until": None},
        ],
        "BMW": [
            {"model": "M5", "production_year": 2010, "rented": False, "rented until": None},
            {"model": "M3", "production_year": 2008, "rented": True, "rented until": None},
        ],
        "MERCEDES": [
            {"model": "GLK", "production_year": 2015, "rented": False, "rented until": None},
            {"model": "GLE", "production_year": 2017, "rented": False, "rented until": None},
        ],
    }

    def __init__(self):
        self.__brand = None
        self.__model = None

        # GET METHODS

    @property
    def model(self):
        if self.__model is None:
            return f"Model not entered yet."
        else:
            return f"Model: {self.__model}"

    @property
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

    @property
    def rented_cars(self):
        if self.brand is None or self.__model is None:
            return f"Enter a brand or model!"

        for car in Car.VALID_CARS:
            if car['model'] == self.__model:
                return

    # SET METHODS

    @brand.setter
    def brand(self, brand):
        brand = brand.upper()
        if not isinstance(brand, str):
            raise ValueError("Brand not entered yet.")
        else:
            if brand in Car.VALID_CARS.keys():
                self.__brand = brand
            else:
                raise ValueError("The brand must be audi, bmw or mercedes!")

    @model.setter
    def model(self, model):
        model = model.upper()
        valid_models = []
        for car in Car.VALID_CARS[self.__brand]:
            valid_models.append(car["model"])

        if model in valid_models:
            self.__model = model
        else:
            raise ValueError(f"Not valid model! Allowed models are {valid_models}")
