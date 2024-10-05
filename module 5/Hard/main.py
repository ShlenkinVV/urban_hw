"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""
from UrTube import *
ur = UrTube()
ur.register('vova', 123, '22')
ur.register('vov', 123, 'CZ')
print(ur.users)


print(ur.current_user)
ur.log_in('vo', '2')
print(ur.current_user)
ur.log_in('vova', '22')
print(ur.current_user)
ur.log_out()
print(ur.current_user)

vids1 = Video('first', 20)
vids2 = Video('second', 20)
vids3 = Video('first', 20)
ur.add(vids1, vids2, vids3)
print(ur.videos)

res1 = ur.get_videos('FIR')
res2 = ur.get_videos('s')
print(res1, res2)

print('=================================================================')
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
