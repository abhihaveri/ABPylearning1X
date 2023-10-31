'''Program 2:
Find the intersection and union of two sets.'''
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

union_sets=set1.union(set2)
intersection_sets=set1.intersection(set2)
print(f"The Union of Set1 and Set2 is {union_sets} and\nThe intersection of set1 and set2  is {intersection_sets}")