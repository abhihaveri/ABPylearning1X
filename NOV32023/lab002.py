# car -
# objects -tesla,lambo

class Car:
    name=None
    color=None
    model=None
    speed=None
    engine=None

#self is a special variable that s ised witihn the context of object oriented programming
# it is a reference to the instance of a class
# access and manipulate the attributes and methods of that instance/Object

    def start_engine(self):
        print("Starting Engine")
    def drive(self):
        print("Drive")
    def car_break(self):
        print("Break")
    def what_is_driving(self):
        print("I am driving " +self.name)

tesla_obj_ref= Car() # instance of the class =object
lambo_obj_ref= Car() # instance of the class =object

tesla_obj_ref.name="tesla 6-model"
lambo_obj_ref.name="lambo super-model"

tesla_obj_ref.what_is_driving()
lambo_obj_ref.what_is_driving()
