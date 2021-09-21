def main():
    n = 6
    A = 1
    B = 1

    while n <= 10:
        C = B
        B = A + B
        A = C
        print(B)
        n += 1

    print('-' * 50)
    print(f'A: {A}')
    print(f'B: {B}')
    print(f'C: {C}')

if __name__ == '__main__':
    main()