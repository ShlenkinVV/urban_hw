"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV

Многопроцессное программирование
"""
import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            all_data.append(line)




if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # # Линейный вызов
    # start_time = time.time()
    # for filename in filenames:
    #     read_info(filename)
    #
    # end_time = time.time()
    # print(f"Время выполнения линейного вызова: {end_time - start_time} секунд")



    # Многопроцессный вызов
    start_time_mp = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)

    end_time_mp = time.time()  # Конец отсчета времени
    print(f"Время выполнения многопроцессного вызова: {end_time_mp - start_time_mp} секунд")