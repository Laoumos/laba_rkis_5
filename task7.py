# Задание 7. Даны координаты точки и радиус круга с центром в начале координат.
# Определите, принадлежит ли данная точка кругу;

def radar(x, y, radius):
    import math
    path = math.sqrt(float(x) ** 2 + float(y) ** 2)
    if path <= radius:
        return True
    else:
        return False


print(radar(0, 5, 5))
# проверял на desmos
