"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['BMW', 5, False]
values_dict = {'a': 23, 'b': "String", 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Duck', 55.55]
print_params(*values_list_2, 30)
