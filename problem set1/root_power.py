import math

def find_result(integer):
    result_list = []
    for pwr in range(1, 625):
        base_root_value = integer ** (1.0 / pwr)
        if int(math.ceil(base_root_value)) ** pwr == integer:
            pair_tuple = tuple([int(math.ceil(base_root_value)), pwr])
            result_list.append(pair_tuple)
    return result_list


try:
    integer = int(input('Enter a integer:'))
    print(find_result(integer))
except:
    print('Invalid input. Try again')