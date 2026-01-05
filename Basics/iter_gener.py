class PowerTwoIterator:
    def __init__(self, max_power):
        self.max = max_power
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        # 1. Manual check for stopping
        if self.current > self.max:
            raise StopIteration
        
        # 2. Calculate result
        result = 2 ** self.current
        
        # 3. Manually update state for next time
        self.current += 1
        return result

# Usage
iter_obj = PowerTwoIterator(3)
print(next(iter_obj)) # 1
print(next(iter_obj)) # 2