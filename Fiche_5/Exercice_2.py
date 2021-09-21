def main():
    a = int(input('a >> ')) + sum(1 for _ in range(1, 5))
    print(a)


if __name__ == '__main__':
    main()