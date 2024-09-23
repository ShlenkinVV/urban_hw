"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()

# inner_function() ошибка, не видит функцию, так как она находится в локальной области видимости функции test_function
