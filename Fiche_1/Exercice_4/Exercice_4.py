def tableau(x):
    a = x ** 2 + 1
    b = 2 * a - 3
    return a, b

def main():
    while True:
        x = int(input('x: '))
        a, b = tableau(x)
        print(f'a = {a}')
        print(f'b = {b}')
        print('-' * 50)

if __name__ == '__main__':
    main()