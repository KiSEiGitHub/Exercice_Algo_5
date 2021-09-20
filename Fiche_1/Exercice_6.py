def j(x):
    y = x + 1
    y = 2 * y
    y = y - x
    return y - 2


def main():
    while True:
        x = int(input('x: '))
        print(j(x))

        print('-' * 50)


if __name__ == '__main__':
    main()