a = 256
b = 256
print(a is b)  # True → same object

a = -912572345123999912572345123999912572345123999912572345123999.123456789
b = -912572345123999912572345123999912572345123999912572345123999.123456789
print(a is b)  # Might be False → different objects
a = "abcde"*1000
b = "abcde"*1000
print(a is b)  # Might be False → different objects
print(id(a), id(b))  # Might be different
