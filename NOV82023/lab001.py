class BankAccount:
    def __init__(self):
        self.balance=0 # Instance Variable (you can access it via object)
        self.__private_var=0

    def deposit(self,amount): #public function
        #self.balance= self.balance + amount
        self.balance+=amount

    def _withdraw(self,amount): #protected
        self.balance -=amount

    def __show_balance(self): #private
        print("yourBal",self.balance)

    def is_Auth_True(self,isAuth):
        if isAuth:
            self.__show_balance()
        else:
            print("Failed Auth")

    def do_withsrwn_by_bank_manager(self,amount):
        self._withdraw(amount=amount)

jp_chase =BankAccount()
jp_chase.deposit(10000)
jp_chase._withdraw(500)

'''#jp_chase.__show_balance()
jp_chase._BankAccount__private_var =100
print(jp_chase._BankAccount__private_var) # super Bad Practise -Python allows this hack'''

jp_chase.is_Auth_True(True)
jp_chase.do_withsrwn_by_bank_manager(200)