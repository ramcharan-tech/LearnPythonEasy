import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_add(x, y):
    #time.sleep(1)
    return x**y+y**x

print(slow_add(3, 5))
