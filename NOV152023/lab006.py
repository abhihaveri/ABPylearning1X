#Collections -

#list,dic.tuple,set,orderedDict ?

from collections import namedtuple

Person = namedtuple("Person",["name","age","gender"])

person =Person(name='Abhishek',age=31,gender='male')

print(person.name)

class Person2:

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def print_details(self):
        print(f"Person Details {self.name}")

person2 =Person2("AbhishekGh",32,"M")
person2.print_details()