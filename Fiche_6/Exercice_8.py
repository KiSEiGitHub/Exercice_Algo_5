def puissance(x, y):
    return x ** y

def main():
    while True:
        n = int(input('n >> '))
        p = int(input('puissance >> '))
        print(puissance(n, p))
        print('-' * 50)


if __name__ == '__main__':
    main()