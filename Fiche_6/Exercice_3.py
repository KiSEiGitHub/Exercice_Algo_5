def main():
    while True:
        s = int(input('s >> ')) + sum(1 for _ in range(101))
        print(s)
        print('-' * 50)


if __name__ == '__main__':
    main()