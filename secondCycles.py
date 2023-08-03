from random import random, randrange, randint
x = randint(0, 1000)
y = randint(0, 1000)
s = x + y
print(f"S = {s}")
p = x * y
print(f"P = {p}")
# подготовили числа, их сумму и произведение
number_1 = 0
for number_1 in range(0, s):
    number_2 = s - number_1 
    if number_1 * number_2 == p :
        print(f"{number_1} and {number_2}")
        break