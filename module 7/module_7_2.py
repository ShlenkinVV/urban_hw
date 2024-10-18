"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""


def custom_write(file_name, strings):
    count_str = 1
    file = open(file_name, 'w', encoding='utf-8')
    res = {}
    for string in strings:
        res[(count_str, file.tell())] = string
        file.write(string + '\n')
        count_str +=1
    file.close()
    return res


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)