class equation:
    def __init__(self):
        self.x = 5

    def fonction_1(self):
        return 2 * self.x ** 2 - 3 * self.x - 20

    def fonction_2(self):
        return -2 * self.x ** 3 + 111 * self.x

    def fonction_3(self):
        return -2 * self.x ** 3 + 27 * self.x ** 2

    def egalite_f_1(self):
        return self.fonction_1() == self.x + 28

    def egalite_f_2(self):
        return self.fonction_2() == self.x ** 3 + 252

    def egalite_f_3(self):
        return self.fonction_3() == 16 * self.x + 240

    def print(self):
        print(f'solution équation 1 = {self.egalite_f_1()}')
        print(f'solution équation 2 = {self.egalite_f_2()}')
        print(f'solution équation 3 = {self.egalite_f_3()}')

def main():
    equation().print()


if __name__ == '__main__':
    main()