x = {1:"swamy",2:"charan",3:"ravali",4: "xyz",5:"abc",6: None}
y = dict()

# HOW TO ADD/UPDATE
x.update({4:"ram"}) # update can add new item
x[5] = "balu" # adding by accessing a key
print("ADD NEW ELEMNT: ", x.setdefault(7)) # if key is present in dict, no updates, it returns value from dict. If key is not present, it adds and returns default_value.
print(x)

# HOW TO DELETE
print(x.popitem()) #popitem needs no arg, it deletes last item, if dict is empty it throws error
print(x.pop(4),"\n") # pop needs a key, it throws error if key is not present
del x[6] # doesn't return value, if key is not present it throws error
# x.clear()

# HOW TO GET

print("GET 1 element: ",x[1]) # it throws error if key is not found
print("GET 1 element: ",x.get(1)) # it gives None if key is not found
print("GET KEYS: ",x.keys())
print("GET VALUES: ",x.values())
print(type(x.items())) # its a dictionary of items
print(x.items())

# HOW TO SEARCH/FIND
print(1 in x) # it finds only keys in dict, not values
print("swamy" in x.values())
x = {"hello" + value:key for key,value in x.items()}
print("Is swamy present: ","swamy" in x)
print("Checking: ",any(z.find("oswamy") > 0 for z in x)) # other functions any, sorted

#HOW TO COPY
y=x.copy()
print("Y elements are copied: ",y)


