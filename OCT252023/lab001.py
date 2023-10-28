#List
my_list =[1,2,3,3]
my_list2 =[1,True,"Promod"]

print("initial list:",my_list)

# Indexing
print("element at index 0:",my_list[0])

#chnagig an element
my_list[1]=20
print(my_list)
print("element after changing element at index  1:",my_list[1])

#append
my_list.append(4)
print("element after append:",my_list)

#extend
my_list.extend([5,6])
print("element after extend:",my_list)

#insert()
my_list.insert(1,25)
print("element after insert at index 1:",my_list)

#Remove()
my_list.remove(25)
print("element after removing 25:",my_list)

#copy()
my_copy_list=my_list.copy()
print("list after copying:",my_copy_list)

#clear()
my_list.clear()
print("list after clearing:",my_list)

#index
#print("list index at 3:",my_list[2])
print("list index at 3:",my_copy_list[2])

my_copy_list.sort()
print('sorting',my_copy_list)
my_copy_list.reverse()
print('reversing',my_copy_list)

print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])
