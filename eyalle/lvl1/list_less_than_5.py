ages = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ages_less_5 = []

for age in ages:
    # print (f'age ==> {age}')
    if (age < 5):
        # print ('LESS THAN 5')
        ages_less_5.append(age)

print (f'ages: {ages_less_5}')