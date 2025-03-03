import math


x= 3
y=3
if x > y:
  print("Greater value is x=",x)
elif x < y:
  print("Greater value is y=",y)
else:
  print("Both are equal")
#-------------------------------------------------------------------------------------
check_pass_fail = lambda score: "Passed" if score > 50 else "Failed"
print(check_pass_fail(50))

#-------------------------------------------------------------------------------------

class something:
  pass
  classvar = 30
  def somemethod(self):
    print("some method")
    pass
  if True:
    print("if loop")
    pass
  for i in range(0,1):
    print("for loop")
    pass
  print("passing")
  @classmethod
  def classdef(cls,x):
    classvar = 20
    print(f"you passed {x} and classvar is {classvar}")
  @staticmethod
  def staticdef():
    x = math.pi
    print("Its just static, you want PI %.7f %exo "%(x,x))
  print(f"{classvar}")

somethin =something()
somethin.classdef(10)
somethin.staticdef()
# somethin.somemethod()
