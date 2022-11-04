import math

x = 2.05
y = 0.95

z = math.pow(x, 3) - math.pow(y, 3)

# print(f'{z:.4f}')

result = 3 * math.pow(x, 3) - 6*math.pow(x, 2) - 3 * \
    math.pow(y, 3) + 3*math.pow(y, 2)+ 7 - z 
print(f'{result:.4f}')