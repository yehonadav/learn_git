from random import randint
import zero_division

def randomly_stringify_list_items(num_list):
    amount_to_str = randint(0,len(num_list))
#     print(f'amount = {amount_to_str}')
    for i in range(0,amount_to_str):
        # print(f'i = {i}')
        to_be_stred = randint(0,len(num_list)-1)
        # print(f'to_be_stred = {to_be_stred}')
        num_list[to_be_stred] = str(num_list[to_be_stred])
    return num_list


if __name__ == "__main__":
    numbers = zero_division.create_numbers()
    zero_division.display_num_list(numbers)
    got_exc = False
    while (not got_exc):
        try:
                zero_division.print_average(randomly_stringify_list_items(numbers))
                numbers = zero_division.create_numbers()
        except Exception:
                got_exc = True
