"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV

Потоки на классах
"""
import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        count = 0
        print(f'{self.name}, на нас напали!')
        while self.enemies:
            self.enemies -= self.power
            count += 1
            print(f'{self.name} сражается {count} день(дня)..., осталось {self.enemies} воинов\n', end='')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {count} дней(дня)!\n', end='')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились')
