import miln
import matplotlib.pyplot as plt
import numpy as np
import math

if __name__ == "__main__":
    print("Выберите функцию:\n1. y' = -sin(x) - y\n2. y' = 2y/(x+1) + x + 1\n3. y' = cos(x) - y\nВведите число от 1 до 3")
    while True:
        try:
            f_type = int(input().strip())
            if f_type > 3 or f_type < 1:
                print("Введите число от 1 до 3")
                continue
            break
        except ValueError:
            print("Неверный формат числа. Введите число от 1 до 3")

    print("Введите начальное условие  - x, y через пробел")
    while True:
        try:
            points = input().strip().split(" ")
            if len(points) != 2:
                print("Введите два числа")
                continue
            points[0] = float(points[0])
            points[1] = float(points[1])
            break
        except ValueError:
            print("Не удалось распознать числа. Попробуйте ещё раз")

    print("Введите точность")
    while True:
        try:
            eps = abs(float(input().strip()))
            break
        except ValueError:
            print("Не удалось распознать число. Попробуйте ещё раз")

    print("Введите конец отрезка")
    while True:
        try:
            end = abs(float(input().strip()))
            break
        except ValueError:
            print("Не удалось распознать число. Попробуйте ещё раз")

    if f_type == 1:
        f = lambda x, y: -math.sin(x) - y
    elif f_type == 2:
        f = lambda x, y: 2*y/(x+1) + x +1
    else:
        f = lambda x, y: math.cos(x) - y
    try:
        result = miln.calcMiln(f, *points, eps, end)
        fig, ax = plt.subplots()
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid()
        result = np.array(result)
        ax.plot(result[:,0], result[:,1], label = "График решений")
        ax.legend()
        plt.show()
    except Exception as inst:
        print(inst.args[0])