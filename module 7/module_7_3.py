"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""

_punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    string = line.lower()
                    for char in string:
                        if char in _punctuation:
                            string = string.replace(char, '')
                    string = string.split()
                    if file_name not in all_words:
                        all_words[file_name] = []
                    all_words[file_name].extend(string)
        return all_words

    def find(self, word):
        res = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word.lower() in words:
                res[name] = words.index(word.lower()) + 1
        return res

    def count(self, word):
        all_words = self.get_all_words()
        res = {}
        for name, words in all_words.items():
            _count = words.count(word.lower())
            res[name] = _count
        return res


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

print('=====================================================')

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
