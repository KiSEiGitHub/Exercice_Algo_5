def condition(a, b):
    if a > b > 0 or b >= a > 0:
        return a + b
    elif a > b:
        return a - b
    else:
        return b - a

def main():
    while True:
        n = int(input('n >> '))
        nn = int(input('n >> '))
        print(condition(n, nn))
        print('-' * 50)


if __name__ == '__main__':
    main()