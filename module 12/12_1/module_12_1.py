"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV

Простые Юнит-Тесты
"""

import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run = runner.Runner('Vova')
        for _ in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    def test_run(self):
        run = runner.Runner('Vova')
        for _ in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run1 = runner.Runner('Vova')
        run2 = runner.Runner('Forest')
        for _ in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance, run2.distance)

if __name__ == '__main__':
    unittest.main()