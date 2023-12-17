# a*x**2 + b*x + c = 0 - общий вид уравнения
# D = b**2 - 4*a*c - дискриминант
# Если D<0, то уравнение не имеет вещественных корней
# Если D=0, то уравнение имеет один корень - x = -b/(2*a)
# Если D>0, то уравнение имеет два корня
# x1 = (-b - D**0.5)/(2*a)
# x2 = (-b + D**0.5)/(2*a)
#
# P.S. D**0.5 - равносильно извлечению квадратного корня


def quadratic_solve(a, b, c):
    discriminant = D(a, b, c)
    if discriminant < 0:
        return "Нет вещественных корней"
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b - D(a, b, c) ** 0.5) / (2 * a)
        root2 = (-b + D(a, b, c) ** 0.5) / (2 * a)
        return root1, root2


def D(a, b, c):
    return b ** 2 - 4 * a * c


L = list(map(float, input("Введите 3 числа через пробел \n").split()))
print(quadratic_solve(*L))  # передать элементы списка L в аргументы функции, используя операцию распаковки
