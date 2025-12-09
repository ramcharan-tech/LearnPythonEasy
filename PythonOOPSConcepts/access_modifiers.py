class MyClass:
    def __init__(self):
        self.public_var = "Public"
        self._protected_var = "Protected"
        self.__private_var = "Private"

    def public_method(self):
        print("Public method")
        self._protected_method()
        self.__private_method()

    def _protected_method(self):
        print("Protected method")

    def __private_method(self):
        print("Private method")

obj = MyClass()
print(obj.public_var) # Output: Public
print(obj._protected_var) # Output: Protected (accessible, but discouraged)
#print(obj.__private_var) # Raises AttributeError (name mangled)
print(obj._MyClass__private_var) # Output: Private (accessible, but strongly discouraged)

obj.public_method()
# Output:
# Public method
# Protected method
# Private method
#obj._protected_method() # Output: Protected method (accessible, but discouraged)
#obj.__private_method() # Raises AttributeError (name mangled)
obj._MyClass__private_method() # Output: Private method (accessible, but strongly discouraged)