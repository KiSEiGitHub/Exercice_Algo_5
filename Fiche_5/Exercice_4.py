def boucle(a, b, c):
    for _ in range(2):
        if a > b:
            b = a
        elif b > c:
            c = b
    return a, b, c

def main():
    while True:
        a = int(input('a >> '))
        b = int(input('b >> '))
        c = int(input('c >> '))
        aa, bb, cc = boucle(a, b, c)
        print(f'a: {aa}')
        print(f'b: {bb}')
        print(f'c: {cc}')
        print('-' * 50)


if __name__ == '__main__':
    main()