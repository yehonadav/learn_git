from random import randint
import sys
sys.path.append("../../")
from exercises.data import get_data


data = get_data(20)

def getAddr(name):
    addresses = []
    for item in data:
        if (name == item['name']):
            addresses.append(item['address'])

    return addresses

def add_random_postal(name_with_addresses):
    num = randint(0,9)*10000 + randint(0,9)*1000 + randint(0,9)*100 + randint(0,9)*10 + randint(0,9)
    if num < 9999:
        num = (f'0{num}')
    return (name_with_addresses + (f'{num}',))

def sum_postal_codes(names_addresses_postals):
    sum_of_postals = 0
    for data_item in names_addresses_postals:
        sum_of_postals += int(data_item[2])
    return sum_of_postals

names = set()
for item in data:
    names.add(item['name'])

output = []
for name in names:
    output.append((name, list(map(lambda name: name, getAddr(name)))))
    # print(output[-1])

# print(output)

for i in range(0, len(output)):
    output[i] = add_random_postal(output[i])


print(sum_postal_codes(output))


