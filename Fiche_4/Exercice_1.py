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

    print('-' * 50)

    print(f'29 / 565 = {bool(29 % 565)}')
    print(f'29 / 6785 = {bool(29 % 6785)}')
    print(f'29 / 646195034 = {bool(29 % 646195034)}')
    print(f'29 / 1970659794 = {bool(29 % 1970659794)}')

if __name__ == '__main__':
    main()