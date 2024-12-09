"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""
import unittest
import logging
from rt_with_exceptions import Runner

logger = logging.getLogger(__name__)

class RunnerTest(unittest.TestCase):


    def test_walk(self):
        try:
            run = Runner('Vova', -2)
            for _ in range(10):
                run.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(run.distance, 50)
        except ValueError as e:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)



    def test_run(self):
        try:
            run = Runner(123)
            for _ in range(10):
                run.run()
            self.assertEqual(run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    def test_challenge(self):
        run1 = Runner('Vova')
        run2 = Runner('Forest')
        for _ in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance, run2.distance)




logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")


if __name__ == '__main__':
    unittest.main()

