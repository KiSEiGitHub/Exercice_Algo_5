import math


def aazr(a):
    b = math.sqrt(a)
    c = round(b)

    if b == c:
        print(f'{a} est un carré parfait')
    else:
        print(f"{a} n'est pas un carré parfait")

    print(f'Valeur de b = {b}')
    print(f'Valeur de c = {c}')


def main():
    while True:
        fez = int(input('n: '))
        aazr(fez)
        print('-' * 50)

if __name__ == '__main__':
    main()