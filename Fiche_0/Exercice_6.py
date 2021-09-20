import math


class cone:
    def __init__(self, hauteur, rayon):
        self.h = hauteur
        self.r = rayon

    def formule(self):
        return 1 / 3 * math.pi * self.r ** 2 * self.h

    def aff(self):
        print(f'Hauteur: {self.h}')
        print(f'Rayon: {self.r}')
        print(f'Volume = {round(self.formule(), 2)} cm³')
        print('-' * 50)


def main():
    while True:
        try:
            a = float(input('n: '))
            b = float(input('n: '))
            c = cone(a, b)
            c.aff()
        except ValueError:
            print('nombre!')


if __name__ == '__main__':
    main()