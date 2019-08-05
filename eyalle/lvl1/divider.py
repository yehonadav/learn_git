num = int(input('please enter a num:\n'))
dividers = []

for i in range (2, num-1):
    if (num % i == 0):
        dividers.append(i)

print (f'Dividers:\n {dividers}')