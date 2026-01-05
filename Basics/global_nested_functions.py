def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25

        num=26
    
    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)

outer_function()
print("Outside both function: ", num)