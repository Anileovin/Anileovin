# Python Dictionaries
# Dictionaries are used to store data values in key: value pairs. A dictionary is a collection
# which is ordered, changeable and do not allow duplicates.
"""

details = {
   "names": "stanley",
   "phone": 8011,
   "city": "abuja",
   "city": "lagos",
}
print(details)

# To get the value key from a dictionary, you are to use the get() method.
city = details.get("city")
print(city)

# To get all keys in a dictionary, you use the keys() method.
print(details.keys())

#To get a list of all the values in a dictionary, you use the values() method.
print(details.values())

# To get each item in a dictionary, as tuple in a list, you use the items() method. 
print(details.items())

# Check if key exists
# To determine if a specified key is present in a dictionary use the "in" keyword

details = {
   "names": "stanley",
   "phone": 8011,
   "city": "abuja",
}
if "phone" in details:
    print("Yes phone is present")
else:
    print("phone is not present")
    
# Change values
details["city"] = "lagos"
print("details")

# to copy a dictionary we use copy() method 
mydetails = details.copy()
print(mydict)
    
# To update dictionary
details.update({"phone": 9011})
print(details)

# Adding Items
details["career"] = "software engineer"
print(details)

#Loop dictionary
details =  {
   "names": "stanley",
   "phone": 8011,
   "city": "abuja",
}
#print all the key names in the dictionary
for x in details:
    print(x)
# or
for x in details.keys():
    print(x)


#print all the values names in the dictionary
for x in details:
    print(details[x])
# or
for x in details.values():
    print(x)


#  to loop through both keys and values we use the .item() function
for x, y in details.items():
    print( x, y)


# to know the length of your dictionary
print(len(details))  # outcome 3 because there are 3 items in the dictionary 


# we use .popitem() to remove the last inserted item from a the dictionary
details.popitem()
print(details)
details['age'] = 19  # updating the list with an age of 19
print(details)


# we use the del keyword to remove the item eith the specified key name
del details['age']
print(details)  # deleting the age item from the list.

# we can also use it to del the whole dictionary "details" but when you print the dictionary
# it will produce an error because the dictionary "details" no longer exist
# del details

# we use the .clear() method to clear all items in the dictionary
details.clear()
print(details)

"""

# Nested dictionary :- "a new dictionary within a dictionary"
myfamily = {
      "child1" : {"name" : "Emil", "year" : 2004},
      "child2" : {"name" : "Tobias", "year" : 2007},
      "child3" : {"name" : "Linus", "year" : 2011}
}
print(myfamily)