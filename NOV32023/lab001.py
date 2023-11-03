# Class and Object In Python.

# Person
# attributes -name,age,phone_no,height,weight,gender,prof
# Methods-can do-> Run(),Sleep(),sing(),talk(),eat(),fight(),learn(),hear(),think()

# objects
# Amit
# Durga
# santhosh-

class Person:
    # attributes
    name = None
    age = None
    phone_no = None
    height = None
    weight = None
    gender = None
    prof = None

    # Methods
    def talk(self):
        print(self.name+" is Talking")

    def sleep(self):
        print(self.name+" is Sleeping")

    def walk(self):
        return "I am walking"

amit_object = Person()
amit_object.name="Amit"
amit_object.age=59
amit_object.gender="male"
amit_object.phone_no="987654321"

print(amit_object) #address
print(amit_object.name)
amit_object.sleep()

durga_object = Person()
durga_object.name="Durga"
durga_object.age=69
durga_object.gender="female"
durga_object.phone_no="997654123"

print(durga_object) # address
print(durga_object.name)
durga_object.sleep()
