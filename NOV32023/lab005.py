# take a input from the user we will create how

class Car:
    color=None
    model=None

    def car_details(self):
        print("Your car details is ",self.color,self.model)

car_color =input("enter the car color")
car_model =input("enter the car model")

car_obj_ref =Car()
car_obj_ref.color=car_color
car_obj_ref.model=car_model


car_obj_ref.car_details()
