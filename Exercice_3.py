def main():
    A = 1
    B = 1

    for _ in range(11):
        C = B
        B = A + B
        A = C
        print(B)


if __name__ == '__main__':
    main()