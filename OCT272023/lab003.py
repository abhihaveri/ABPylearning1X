#merging of tuples

hero1=("wonderwomen","Batman")
hero2=("Superman","Thunder")
Team_hero=hero1+hero2
print(Team_hero)

#converting to list
a=(1,2,3)
b=list(a)
print(a)
print(b)

#Nested of tuples

hero1=("wonderwomen","Batman")
hero2=("Superman","Thunder")
awsome_Team=(hero1,hero2)
print(awsome_Team)
print(awsome_Team[0])
print(awsome_Team[1][1])
print(awsome_Team[1])

# Search in tuple

cities =("London","paris","germany")
print("London" in cities)
print("Delhi" in cities)