'''Program 4:
Remove a key-value pair from the dictionary.'''

my_dic ={'a':1,'b':2,'c':3,'a':50}
print(f"The main Dic items: {my_dic}")
val=my_dic.pop('a')
print(f"Removing a particular value {my_dic}")
# removing orbitararily
my_dic ={'a':1,'b':2,'c':3,'a':50}
val_pop_item=my_dic.popitem() # orbitary items (random items will be removed
print(f"Removing a orbitaroryly value {my_dic}")