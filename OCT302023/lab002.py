phone_book={"Batman":987654321,"superman":12345690,"Wonder":55698521}

#dict ? its is very cloase to the Json
print(  phone_book)
print(len(phone_book))

print(phone_book["Batman"])
print(phone_book["Wonder"])

# you can acess element by key only -DIct

phone_book2=dict (Batman=987654321,superman=12345690,Wonder=55698521)
print(phone_book2["Wonder"])
print(phone_book2.get("Wonder"))

promod_details=dict (name="Promod",age=31,isMale=True,Address="KA")
promod_details2= {"name":"Promod","age":31,"isMale":True,"Address":"KA"}
print(promod_details)
print(promod_details["age"])
print(promod_details.get("name"))