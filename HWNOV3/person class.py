# Create a Class Person , Two Objects by taking (name, age, address) Input from users and print details in the end.
class Person:

    '''name = None
    age = None
    address = None'''

    def the_details(self):
        print("The Details of the Person \nName::",self.name)
        print("Age::",self.age)
        print("address::",self.address )


name = input("Please enter the name::")
age = input("Please enter the age::")
address = input("Please enter the address::")

person1_obj_ref = Person()

person1_obj_ref.name = name
person1_obj_ref.age = age
person1_obj_ref.address = address

person1_obj_ref.the_details()
