class Password :

    def __init__(self,password):
        self.__password =password

    def get_password(self,isAuth):
        if isAuth:
            return self.__password
        else:
            print('error**')

    def set_password(self,password):
        if len(password)>10:
            self.__password=password
        else:
            print("weak password")

    def print_len(self):
        print("your pass len is ",len(self.__password),self.__password)

pwd =Password("Hack20230")
pwd.print_len()

pssd=pwd.get_password(True)
print(pssd)

pwd.set_password("prod1232143j")
pwd.print_len()