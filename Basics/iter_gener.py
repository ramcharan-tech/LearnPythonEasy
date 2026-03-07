class PowerTwoIterator:
    def __init__(self, max_power):
        self.max = max_power
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        result = 2 ** self.current

        self.current += 1
        return result

iter_obj = PowerTwoIterator(3)
print(next(iter_obj)) # 1
print(next(iter_obj)) # 2

def power_two_generator(max_power):
    current = 0
    while current <= max_power:
        yield 2 ** current
        current += 1
gen_obj = power_two_generator(3)
print(next(gen_obj))
print(next(gen_obj))