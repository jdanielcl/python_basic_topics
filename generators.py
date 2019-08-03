def numbersGenerator(limit):
    num = 1
    while num < limit:
        yield num*2
        num = num +1
    
numbers = numbersGenerator(10)
print([c for c in numbers])

# numbers = numbersGenerator(10)
# print(next(numbers))
# print('lap')
# print(next(numbers))
# print('lap')
# print(next(numbers))
# print('lap')
# print(next(numbers))
# print('lap')

def cities(*cities):
    for e in cities:
        # hace un for anidado dentro de cada ciudad
        yield from e

cities_test = cities("Bogotá","Medellín","Cali","Arménia","Manizales")

print(next(cities_test))
print(next(cities_test))