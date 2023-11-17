class Myclass:

    def __init__(self):
        self.__private_toilet="Private toilet Only Promod allowed"
        self._protected_toilet = 42
        self.public_toilet = 50

    def __private_method(self):
        return" this is a private method"

obj =Myclass()
'''print(obj.__private_toilet)
print(obj._protected_attribute)'''
obj.public_toilet


# search about the private,protected and public variables
# rewatch the video