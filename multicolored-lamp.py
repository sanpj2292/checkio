class Lamp:

    def __init__(self, i=0):
        self.i = i
        self.colors = ('Green', 'Red', 'Blue', 'Yellow')

    def light(self):
        color = self.colors[self.i % 4]
        self.i += 1
        return color


lamp1 = Lamp()
print('Lamp-1')
print(lamp1.light())
print(lamp1.light())
print(lamp1.light())
print(lamp1.light())

print(lamp1.light())
print(lamp1.light())
print(lamp1.light())
print(lamp1.light())

print(lamp1.light())
print(lamp1.light())
print(lamp1.light())
print(lamp1.light())
