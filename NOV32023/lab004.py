class Myclass:
    #name=None
    def print_my_name(self):
        print("your name is "+self.name)

    def print_my_name_with_last_name(self,name,last_name,age):
        print("your fname and lname are -->" + name ,last_name,age)

promod_obj_ref=  Myclass()
promod_obj_ref.name="Abhishu"
promod_obj_ref.print_my_name()
promod_obj_ref.print_my_name_with_last_name("Abhishek","Haveri",31)