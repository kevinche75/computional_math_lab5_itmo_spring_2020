limit = 100000

def calcRKmethod(f, x, y, h):
    result = []
    result.append([x,y])
    for i in range(3):
        k1 = f(*result[i])
        k2 = f(result[i][0] + h/2, result[i][1] + k1*h/2)
        k3 = f(result[i][0] + h/2, result[i][1] + k2*h/2)
        k4 = f(result[i][0] + h  , result[i][1] + k3*h  )
        result.append([
            result[i][0] + h,
            result[i][1] + h/6*(k1 + 2*k2 + 2*k3 + k4)
            ])
    return result

def predict(f, h, points):
    return points[0][1] + 4*h/3*(
        2*f(*points[1]) - f(*points[2]) + 2 * f(*points[3])
    )

def correct(f, h, points):
    return points[0][1] + h/3*(
        f(*points[0]) + 4*f(*points[1]) + f(*points[2])
    )

def initMiln(f, x, y, eps):
    h = 1.0
    i = 0
    while True:
        i+=1
        if i > limit:
            raise Exception("Ошибка. Не удалось вычислить начальные точки и шаг за {0} итераций".format(limit))
        first_points = calcRKmethod(f, x, y, h)
        y_pr = predict(f, h, first_points[0:])
        first_points.append([
            first_points[3][0] + h,
            y_pr
        ])
        y_cr = correct(f, h, first_points[2:])
        if abs(y_pr-y_cr)/29 <= eps:
            first_points[4][1] = y_cr
            return first_points, h
        h /=2

def calcMiln(f, x, y, eps, end):
    result, h = initMiln(f, x, y, eps)
    x_i = result[4][0]
    i = 4
    while x_i < end:
        i += 1
        x_i += h
        y_pr = predict(f, h, result[i-4:])
        result.append([
            x_i,
            y_pr
        ])
        y_cr = correct(f, h, result[i-2:])
        j = 0
        while abs(y_cr - result[i][1]) > eps:
            j += 1
            if j > limit:
                raise Exception("Ошибка. Не удалось вычислить y_{0} за {1} итераций".format(i, limit))
            result[i][1] = y_cr
            y_cr = correct(f, h, result[i-2:])
        result[i][1] = y_cr
    return result

