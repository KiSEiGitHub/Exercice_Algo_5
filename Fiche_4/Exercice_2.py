def main():
    while True:
        a = int(input('n >> '))
        print(f'{a} / 13 = {bool(a % 13)}')
        print('-' * 50)


if __name__ == '__main__':
    main()