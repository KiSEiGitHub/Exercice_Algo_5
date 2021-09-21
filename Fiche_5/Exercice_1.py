class boucle:
    def __init__(self, n):
        self.n = n

    def algo_1(self):
        while self.n < 50:
            self.n += 1

        print(self.n)

    def algo_2(self):
        while self.n < 50:
            self.n += 1
            print(self.n)


def main():
    while True:
        a = int(input('n >> '))
        b = boucle(a)
        b.algo_2()
        print('-' * 50)
        b.algo_1()


if __name__ == '__main__':
    main()