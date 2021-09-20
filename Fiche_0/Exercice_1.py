from dataclasses import dataclass


@dataclass
class fonction:
    x: int

    def f(self):
        return 2 * self.x + 3

    def g(self):
        return - 2 * self.x ** 2 + 3 * self.x - 7


def affichF(a, b, c, d):
    print(f'f(0) = {a}')
    print(f'f(1) = {b}')
    print(f'f(-3) = {c}')
    print(f'f(-8,5) = {d}')

    print('-' * 50)

def affichG(a, b, c):
    print(f'g(-5) = {a}')
    print(f'g(14) = {b}')
    print(f'g(145) = {c}')

def main():
    un = fonction(0)
    deux = fonction(1)
    trois = fonction(-3)
    quatre = fonction(-8.5)

    affichF(un.f(), deux.f(), trois.f(), quatre.f())

    a = fonction(-5)
    b = fonction(14)
    c = fonction(145)

    affichG(a.g(), b.g(), c.g())


if __name__ == '__main__':
    main()