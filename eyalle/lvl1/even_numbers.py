from number_generator import numbers

class MaxLengthException(Exception):
    # logger.error("list too long")
    def __init__(self):
        super().__init__("list of evens is too long")
    pass
    

even_list = [x for x in numbers(40) if x%2==0]

# try:
#     if (len(even_list) > 10):
#         raise MaxLengthException
#     else:
#         print(f'length of list is {len(even_list)}')
# except MaxLengthException:
#     print("list is too long")

print (f'list length {len(even_list)}')

if (len(even_list) > 10):
    raise MaxLengthException()