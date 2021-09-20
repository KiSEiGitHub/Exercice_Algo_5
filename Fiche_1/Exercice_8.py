def j(x, y):
    x = x - y
    y = x + y
    x = y - x
    return x, y


def main():
    while True:
        x = int(input('x: '))
        y = int(input('y: '))
        a, b = j(x, y)
        print(f'x = {a}')
        print(f'y = {b}')
        print('-' * 50)


if __name__ == '__main__':
    main()