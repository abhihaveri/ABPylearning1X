# order Dict
my_dic ={'a':1,'b':2,'c':3,'a':50}
print(my_dic)

# KEY VALUE PAIRS BASED ON THE ORDER OF INSERTION
#list set tuple dict orderddict -API Automation testing

from collections import OrderedDict
od =OrderedDict()
od['a']=45
od['c']=78
od['b']=66
od['d']=12
print(od)

# seleinum -Insert web elemenst into Dict
# you wnat to keep the order -login eleents,dashboard elements

# dict -it will niot keep the Order of insertion
# OrdertDict- it will keep the order of insertion

keys =list(od.keys())
print(keys)
values=list(od.values())
print(values)

keys_sorted=sorted(keys)
print(keys_sorted)

od2 =OrderedDict()
od2[keys_sorted[0]]=20
od2[keys_sorted[1]]=30
od2[keys_sorted[2]]=40
od2[keys_sorted[3]]=50

print(od2)

keys_sorted=sorted(keys,reverse=True)
print(keys_sorted)
od2 =OrderedDict()
od2[keys_sorted[0]]=20
od2[keys_sorted[1]]=30
od2[keys_sorted[2]]=40
od2[keys_sorted[3]]=50

print(od2)