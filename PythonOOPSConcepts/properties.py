class Celsius:
    def __init__(self, temp=0):
        self._temp = temp

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._temp = value

c = Celsius(25)
print(c.temp)    # 25
c.temp = 30
# c.temp = -300  # ValueError
