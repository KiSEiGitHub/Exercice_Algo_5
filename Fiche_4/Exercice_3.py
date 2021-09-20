def fonction(x, y):
    if x < 5 * y:
        x = 10 * x
    else:
        y = 10 * y
    return x, y

def main():
    while True:
        a = int(input('x >> '))
        b = int(input('y >> '))
        x, y = fonction(a, b)
        print(f'x = {x}')
        print(f'y = {y}')
        print('-' * 50)


if __name__ == '__main__':
    main()