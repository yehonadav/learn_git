import sys
sys.path.append("../../")
from exercises.data import get_data

data = get_data(10)
# print (data)

found = False
for item in data:
    if (item['age'] < 13):
        found = True
        for k, v in item.items():
            print (f'{k} ==> {v}')
        break


if (not found):
    print('All people are old..')
    