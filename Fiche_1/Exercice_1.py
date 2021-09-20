def fonction(a):
    b = 5
    c = a * b
    a = c + 4
    return a, b, c

def main():
    while True:
        n = int(input('A: '))
        x, y, z = fonction(n)
        print(f'a: {x}')
        print(f'b: {y}')
        print(f'c: {z}')
        print('-' * 50)


if __name__ == '__main__':
    main()