def main():
    a = int(input('a >> '))
    b = int(input('b >> '))
    c = int(input('c >> '))

    if a < b < c or b <= a < c:
        print(f'{c} est plus grand')
    elif a < b:
        print(f'{b} est plus grand')
    else:
        print(f'{a} est plus grand')

if __name__ == '__main__':
    main()