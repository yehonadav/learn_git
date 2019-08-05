import time

fibonacci_sum = 0
i = 0
y = 1
# print (f'{i}\n{y}\n')
while True:
    fibonacci_sum += y
    # print (f'fib {fibonacci_sum}')
    y = i
    print (f'{y}')
    i = fibonacci_sum
    # print (f'i {i}')
    time.sleep(1)