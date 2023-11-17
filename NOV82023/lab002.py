class Person:
    def __init__(self,name,age):
        self.__name =name
        self.__age=age

    def print_details(self):
        print("your Details",self.__name,self.__age)

    def get_name(self):
        return self.__name

    def set_name(self):
        if name =="john":
            print("Dont Set the name")
        else:
            self.__name


person =Person("Amit",34)
person.print_details()

print(person.__name) #Private ?

'''how to change it ans set ?
Fetch -Get
Set the value '''

print(set_name)
