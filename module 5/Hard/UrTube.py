"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""
from time import sleep
from User import User
from Video import Video


class UrTube:
    def __init__(self, current_user=None):
        self.users = []
        self.videos = []
        self.current_user = current_user

    def log_in(self, nickname, password):
        exist = False
        password_hash = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                exist = True
                if password_hash == user.password:
                    self.current_user = user
                    print(f'Привет, {nickname}')
                else:
                    print('Неверный пароль')
        if not exist:
            print('Пользователь не найден')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, age, password)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(existing_video.title == video.title for existing_video in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        result = []
        search_word_lower = search_word.lower()
        for video in self.videos:
            if search_word_lower in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == title:
                if self.current_user.age >= 18 or video.adult_mode == False:
                    for i in range(video.time_now, video.duration+1):
                        print(i)
                        sleep(1)
                    print('Конец фильма')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')


