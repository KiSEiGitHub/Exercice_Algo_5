import math
import matplotlib.pyplot as plt

def f():
    fonction_f = []
    for i in range(10):
        a = math.sqrt(9 - i)
        fonction_f.append(a)
    return fonction_f

def g():
    fonction_g = []
    for i in range(3, 12):
        a = math.sqrt(2 * i - 6)
        fonction_g.append(a)
    return fonction_g


def main():
    courbe_f = f()
    courbe_g = g()

    plt.plot(courbe_f)
    plt.title('Fonction f')
    plt.show()

    plt.plot(courbe_g)
    plt.title('Fonction g')
    plt.show()

if __name__ == '__main__':
    main()