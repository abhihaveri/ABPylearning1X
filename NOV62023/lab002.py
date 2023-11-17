class Person:
    name ="Amit"  #class variable

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("You created an object")

    def printdetails1(self):
        print("Your details are",self.name,self.age)

    def printdetails2(self):
        print("Your details are",self.name*2,self.age)

abhi=Person("Abhishek",31)
abhi.printdetails1()

souj=Person("Soujanya",29)
souj.printdetails2()
