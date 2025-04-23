import matplotlib.pyplot as plt


def Ellips(h, k, a, b):
    x = 0
    y = b
    x_list = []
    y_list = []
    p1 = b * b - a * a * b + a * a / 4
    while b ** 2 * x <= a ** 2 * y:
        x_list.append([x + h, -x + h, x + h, -x + h])
        y_list.append([y + k, y + k, -y + k, -y + k])

        x = x + 1
        if p1 < 0:
            p1 = p1 + 2 * b ** 2 * x + b ** 2
        else:
            y = y - 1
            p1 = p1 + 2 * b ** 2 * x - 2 * a ** 2 * y + b ** 2

    p2 = b ** 2 * (x + 0.5) ** 2 + a ** 2 * (y - 1) ** 2 - a ** 2 * b ** 2
    while y >= 0:
        x_list.append([x + h, -x + h, x + h, -x + h])
        y_list.append([y + k, y + k, -y + k, -y + k])

        y = y - 1
        if p2 > 0:
            p2 = p2 - 2 * a ** 2 * y + a ** 2
        else:
            x = x + 1
            p2 = p2 + 2 * b ** 2 * x - 2 * a ** 2 * y + a ** 2

    return x_list, y_list

h = 2
k = 3
a = 10
b = 5
x_list, y_list = Ellips(h, k, a, b)
plt.scatter(x_list, y_list)
plt.show()