def equation(x):
    y1 = x ** 2 - 5
    y2 = -3 * x ** 2 + 8 * x + 7
    return y1, y2

def main():
    a, b = equation(0)
    print(f'y1 = {a}')
    print(f'y2 = {b}')


if __name__ == '__main__':
    main()