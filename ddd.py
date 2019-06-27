from collections import namedtuple

Car = namedtuple('Car', 'model, volume, price')
mycar = Car('BMW', 3000, 22.0)

print(mycar)
print(mycar.model)
print(mycar[0])
#print(mycar['model']) ERROR
