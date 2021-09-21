class multiple_boucle:

    @staticmethod
    def boucle_1():
        for i in range(10):
            print(i)

    @staticmethod
    def boucle_2():
        for n in range(16, 0, -1):
            print(n)

    @staticmethod
    def boucle_3():
        for i in range(18, 45):
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