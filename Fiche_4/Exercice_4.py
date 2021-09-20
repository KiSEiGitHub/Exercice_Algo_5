def main():
    a = int(input('a >> '))
    b = int(input('b >> '))
    c = int(input('c >> '))

    M = a ** 2
    N = b ** 2
    x = M + N
    y = c ** 2

    if x == y:
        print('C\'est un triangle rectangle')
    else:
        print("Ce n'est pas un triangle rectangle")

if __name__ == '__main__':
    main()