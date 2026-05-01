

from models.User import *
from models.Car import Car



# CREATE USER METHOD
option = None
available_options = [1,2,3,4]
while option not in available_options:
    while option is None:
        option = int(input("1. Create user\n"
                           "2. Read Users\n"
                           "3. Free vehicle for rent\n"
                           "4. busy vehicle for rent\n"
                           "5. Exit\n"
                           "Your choice:"))

        if option not in available_options:
            raise ValueError("Invalid option!")


        if option == 1:
            user = User()
            user.name = input("Please enter user name and last name: ")
            user.age = int(input("Please enter user age: "))
            user.create()
            option = None
        elif option == 2:
            for u in User.users:
                print("Users:")
                print (f"- {u} \n")
            option = None

        elif option == 3 or 4:

            for brand in Car.VALID_CARS:
                print (f"\n{brand} ")
                for car in Car.VALID_CARS[brand]:
                    if not car['rented'] and option == 3:
                        print (f"- model: {car['model']}")

                    elif car['rented'] and option == 4:
                        print (f"- model: {car['model']}")

            option = None


        elif option == 5:
            exit()









