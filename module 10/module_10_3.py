"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV

Блокировки и обработка ошибок
"""
import threading
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            sum_ = randint(50, 500)
            self.balance += sum_
            if self.balance>=500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {sum_}. Баланс: {self.balance}\n', end='')
            sleep(0.001)

    def take(self):
        for i in range(100):
            sum_ = randint(50, 500)
            print(f'Запрос на {sum_}\n', end='')
            if sum_ <= self.balance:
                self.balance -= sum_
                print(f'Снятие: {sum_}. Баланс: {self.balance}\n', end='')
            else:
                print('Запрос отклонён, недостаточно средств\n', end='')
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')