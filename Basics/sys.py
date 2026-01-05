import sys

a = []
print(sys.getrefcount(a))  # Usually 2 (one from `a`, one from function call) refcountingandGC