"""
        ************** TUPLES ***************
"""

# tuples can't be rewrited

a = (10,1)
print(a)
print(a[1])

# separate values from tuples
info = 'Bogota','Colombia','America','Tierra'
city,country,continent,planet=info

print(city+" "+planet)

"""
        ************** LISTS ***************
"""

# the lists are dinamics 

list_one = [1,2,3,4,5]
list_two = [1,2,3,4,5]

print(list_one)

# replace a value
list_one[1] = 10
print(list_one)

# add value
list_one.append(13)
print(list_one)

# retrive a range of values
print(list_one[3:5])

# delete the first element
list_one.pop(0)
print(list_one)

# join two lists
list_one.extend(list_two)
print(list_one)

# get index of a element
print(list_one.index(13))

# check if an element is in the list
print(30 in list_one)
print(3 in list_one)

# Delete the first element given in the list by value
list_one.remove(3)
print(list_one)

# lenght
print(len(list_one))

# how many elements with the same value
print(list_one.count(4))

"""
        ************** SETS ***************
"""

# sets are unordered
thisset = {"apple", "banana", "cherry"}
print(thisset)

# You can't access to an specific object in a set, you need to iterate it
# print(thisset[1])

for x in thisset:
    print(x)

# you can add new values

thisset.add("orange")
print(thisset)
thisset.update(["orange", "mango", "grapes"])
print(thisset)

# Sets can't allow duplicate items

thisset.add("orange")
thisset.add("orange")
thisset.update(["orange", "mango", "grapes"])
print(thisset)

"""
        ************** DICTIONARIES ***************
"""

dictionary = {
    'name': 'Joseph',
    'country': 'EU',
    'account': 1000,
    'delete_me': 'bye world!'
}
dictionary[2] = 2000
del dictionary['delete_me']
print(dictionary)

print(dictionary['name'])