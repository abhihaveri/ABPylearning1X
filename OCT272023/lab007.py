t=("TheTestingAcademy","for","TheTestingAcademy")
print("\n set with the use of Tuple")
print(set(t))

set1={1,2,3,4,5}
set2={2,3,4}

my_set= set1.intersection(set2)
my_set2=set2.intersection(set1)
my_set3=set1.union(set2)
my_set4=set2.issubset(set1)
my_set5=set1.difference(set2)
print(my_set)
print(my_set2)
print(my_set3)
print(my_set4)
print(my_set5)