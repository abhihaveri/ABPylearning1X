#Encapsulation
#data members (attributes) and methods together i a class
#person--> name.age and eat(), sleep()


#public,protected,private -->variables

class Myclass:

    def __init__(self):
        self.public_var=10
        self._protected_var=12
        self.__private_var=15

    def public_method(self):
        print("This is a Public Method")
        print("Only I can see the public value",self.public_var)

    def _protected_method(self):
        print("This is a Public Method")
        print("Only I can see the protected value", self._protected_var)

    def __private_method(self):
        print("This is a Public Method")
        print("Only I can see the private value", self.__private_var)

obj=Myclass()
obj.public_var =34
print(obj.public_var)
obj.public_method()

obj.__private_var =99
print(obj.__private_var)

obj._protected_var =91
print(obj._protected_var)


