x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("1. ",x) 
    inner()
    print("2. ",x) 
outer()
print("3. ",x) 
