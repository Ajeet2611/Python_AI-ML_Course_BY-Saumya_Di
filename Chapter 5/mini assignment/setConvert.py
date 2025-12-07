#Try to add both integer 9 and float 9.0 to a set and observe what happens.
# Hint: you Can Convert one into a sting to make both unique.
my_set = set()
print("empty set is :" , my_set)

my_set.add(9)  #adding integer 9 to set

print("set after adding integer 9 is :" , my_set)

my_set.add(9.0)  #adding float 9.0 to set
print("set after adding float 9.0 is :" , my_set)
#observe that set contains only one item because 9 and 9.0 are considered equal
print("length of set is : ", len(my_set))  #length of set is 1

#prnt set all items
print("set item is : " , my_set)#set item is :  {9} bicause 9 and 9.0 are considered same