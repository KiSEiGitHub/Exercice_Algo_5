def tableau(x):
    x += 2
    a = x - 1
    b = 2 * a
    c = b / 2
    return c + 2

def main():
    while True:
        x = int(input('x: '))
        d = tableau(x)
        print(f'd = {d}')


if __name__ == '__main__':
    main()