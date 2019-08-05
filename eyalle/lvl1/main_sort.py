import sys, time
sys.path.append("../../")
from exercises.data import get_data
from exercises.level_1.sort_data import sort_names_with_addresses, add_random_postal, sum_postal_codes

def main():
    divider="""
===================================================
===================================================\n\n
    """
    print('Getting data..')
    data = get_data(30)
    print(divider)
    time.sleep(1)

    print('sorting names with addresses')
    sorted_data = sort_names_with_addresses(data)
    print(sorted_data)
    print(divider)
    time.sleep(1)

    print('adding random postals')
    data_with_postals = add_random_postal(sorted_data)
    print(data_with_postals)
    print(divider)
    time.sleep(1)

    print(f'sum of postals: {sum_postal_codes(data_with_postals)}')



if __name__ == "__main__":
    main()