#dict
my_dict={'a':1,'b':2,'c':3,'a':50}
print(my_dict)

#latest values of key is used

keys=my_dict.keys()
values=my_dict.values()
print(keys)
print(values)

list_keys=list(keys)
print(list_keys)
print(list_keys[0])
print(list_keys[-1])

my_dic ={'a':1,'b':2,'c':3,'a':50}

#dict -key and value
print('before',my_dic)
my_dic.clear()
print('after',my_dic)

my_dic ={'a':1,'b':2,'c':3,'a':50}
copy_dict=my_dict.copy()
print(copy_dict)



