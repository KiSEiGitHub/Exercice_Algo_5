class multiple_boucle:

    @staticmethod
    def boucle_1():
        n = 0
        while n < 10:
            print(n)
            n += 2

    @staticmethod
    def boucle_3():
        for n in range(50, 150):
            if n % 2 == 1:
                print(n)

    @staticmethod
    def boucle_2():
        for i in range(18, 45):
            if i % 2 == 0:
                print(i)


def main():
    print('Boucle 1')
    multiple_boucle.boucle_1()
    print('-' * 50)

    print('Boucle 2')
    multiple_boucle.boucle_2()
    print('-' * 50)

    print('Boucle 3')
    multiple_boucle.boucle_3()


if __name__ == '__main__':
    main()