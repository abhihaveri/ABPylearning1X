# Create a Car class and Create 2 Objects of the class with attributes 5 and 5 methods

class Car:
    model = None
    color = None
    name = None
    variant = None
    speed = None

    def basic_details(self):
        print(f"The basic details of the Car are :-{self.variant} varient,{self.name},{self.model} Model")

    def color_car(self):
        print("The Car color is :",self.color)

    def model_details(self):
        if self.model > 1900:
            print(f"The Car is new model i.e year::{self.model}, {self.name}")
        else:
            print(f"The Car is old model i.e year:: {self.model} build {self.name}")

    def petrol_deisel(self):
        print(f"the  {self.name}  is  {self.variant} Engine")

    def speed_details(self):
        print("the speed of Car is " + self.speed)

maruti_obj_ref = Car()
Hyundai_obj_ref = Car()

# attributes for Obj 1
maruti_obj_ref.name = "Maruthi Baleno"
maruti_obj_ref.variant = 'Petrol'
maruti_obj_ref.speed = '70 kmph'
maruti_obj_ref.model = 1899
maruti_obj_ref.color = 'Green'
print("**********Maruthi***************")
maruti_obj_ref.basic_details()
maruti_obj_ref.color_car()
maruti_obj_ref.petrol_deisel()
maruti_obj_ref.model_details()
maruti_obj_ref.speed_details()
print("**********End***************")
# attributes for Obj 2
Hyundai_obj_ref.name = "Hyundai I20"
Hyundai_obj_ref.variant = 'Diesel'
Hyundai_obj_ref.speed = '80 kmph'
Hyundai_obj_ref.model = 2000
Hyundai_obj_ref.color = 'Pink'
print("**********Hyundai***************")
Hyundai_obj_ref.basic_details()
Hyundai_obj_ref.color_car()
Hyundai_obj_ref.petrol_deisel()
Hyundai_obj_ref.model_details()
Hyundai_obj_ref.speed_details()
print("**********End***************")