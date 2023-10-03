basic_int1 = basic_int2 = 'hello'
basic_int2 = 6
_privat ="private"
print(basic_int1, basic_int2)
float1 = 5.0
comp1 = 1+6j
print(float1,'is the type of',type(float1))
print(comp1,'is the type of',type(comp1))

x = 5
y = 10
print('New Year', 2023, 'See you soon!', sep= '. ',end=' ')
print('The value of x is {} and y is {}'.format(x,y))

def outerfunc():
    global basic_int1 
    basic_int1 = 'mell'
    for x in basic_int1:
        if x=='l':
          print(x)
          break
    else:
        print("no items left")

outerfunc()

counter = 0

while counter < 3:
    # loop ends because of break
    # the else part is not executed 
    # if counter == 1:
    #     continue

    print('Inside loop')
    counter = counter + 1
else:
    print(pow(2,3))

