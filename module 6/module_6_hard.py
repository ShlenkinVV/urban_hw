"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""
import math


class Figure:
    sides_count = 0

    def __init__(self, colors, *sides, filled=True):
        self.__colors = colors
        self.__sides = list(sides)
        self.filled = filled

    def get_color(self):
        return self.__colors

    def __is_valid_color(self, r, g, b):
        return (isinstance(r, int) and 0 <= r <= 255) and \
            (isinstance(g, int) and 0 <= g <= 255) and \
            (isinstance(b, int) and 0 <= b <= 255)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__colors = (r, g, b)
        else:
            print('Неккоретно введен новый цвет')

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != len(self.__sides):
            return False
        return all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print('Некорректно введены стороны')


class Circle(Figure):
    sides_count = 1

    def __init__(self, colors, *sides, filled=True):
        if len(sides) != self.sides_count:
            sides = [1]
        super().__init__(colors, *sides, filled=filled)
        self.__radius = sides[0] / (math.pi * 2)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, colors, *sides, filled=True):
        if len(sides) != self.sides_count:
            sides = [1, 1, 1]
        super().__init__(colors, *sides, filled=filled)

    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, colors, *sides, filled=True):
        if len(sides) != 1:
            sides = [1] * 12
        else:
            sides = [sides[0]]*12
        super().__init__(colors, *sides, filled=filled)

    def get_volume(self):
        sides = self.get_sides()
        return sides[0]**3


circle1 = Circle((200, 200, 100), 10)
print('Стороны круга1:', circle1.get_sides())
print('Площадь круга1:', circle1.get_square())

circle2 = Circle((200, 200, 100), 2, 2, 2, 2, 2)
print('Стороны круга2:', circle2.get_sides())
print('Площадь круга2:', circle2.get_square())

triangle1 = Triangle((200, 200, 100), 2, 2, math.sqrt(8))
print('Стороны треуголника:', triangle1.get_sides())
print('Площадь треугольника:', triangle1.get_square())

cube1 = Cube((200, 200, 100), 2, 2, 2, 2, 2)
print('Стороны куба1:', cube1.get_sides())
print('Объем куба1:', cube1.get_volume())

cube2= Cube((200, 200, 100), 6)
print('Стороны куба2:', cube2.get_sides())
print('Объем куба2:', cube2.get_volume())

print('==================================================================')

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
