"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV

Методы Юнит-тестирования
"""
import sys

from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for res in cls.all_results.values():
            for key, value in res.items():
                print(f'{key}: {value}', end=' ')
                sys.stdout.flush() # без этого метода не работает функция print с параметром end
            print()


    def test_run1(self):
        tr = Tournament(90, self.runner1, self.runner3)
        result = tr.start()
        TournamentTest.all_results['run1'] = result
        self.assertTrue(result[max(result)].name == self.runner3.name)

    def test_run2(self):
        tr = Tournament(90, self.runner2, self.runner3)
        result = tr.start()
        TournamentTest.all_results['run2'] = result
        self.assertTrue(result[max(result)].name == self.runner3.name)

    def test_run3(self):
        tr = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tr.start()
        TournamentTest.all_results['run3'] = result
        self.assertTrue(result[max(result)].name == self.runner3.name)

    def test_run4(self):
        tr = Tournament(3, self.runner3, self.runner2, self.runner1)
        result = tr.start()
        TournamentTest.all_results['run4'] = tr.start()
        self.assertTrue(result[max(result)].name == self.runner3.name)

    def test_run5(self):
        tr = Tournament(5, self.runner2, self.runner3, self.runner1)
        result = tr.start()
        TournamentTest.all_results['run4'] = tr.start()
        self.assertTrue(result[max(result)].name == self.runner3.name)

if __name__ == '__main__':
    unittest.main()
