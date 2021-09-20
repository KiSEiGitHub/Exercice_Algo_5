def formule(a, b):
    if 3 * a < b:
        a = 3 * a
    else:
        b = 3 * b

    print(f'a = {a}')
    print(f'b = {b}')
    print(a + b)

def main():
    while True:
        dfgs = int(input('a: '))
        fegz = int(input('b: '))
        formule(dfgs, fegz)
        print('-' * 50)

if __name__ == '__main__':
    main()