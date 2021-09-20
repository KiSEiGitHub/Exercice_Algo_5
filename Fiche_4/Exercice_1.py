def main():
    a = int(input('a >> '))
    b = a / 13
    c = a // 13

    if b == c:
        print(True)

    else:
        print(False)

    print(f'b = {b}')
    print(f'c = {c}')

if __name__ == '__main__':
    main()