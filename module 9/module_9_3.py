"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV


Генераторные сборки
1. Выдают результат только тогда, когда надо, то есть вычисляются при необходимости;
2. Могут выполниться только один раз.
3. Занимают мало места в памяти.
"""

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))