class equation:

    @staticmethod
    def f():
        for i in range(1, 11):
            print(f'f({i}) = {i ** 2 - 5}')

    @staticmethod
    def g():
        for i in range(1, 11):
            print(f'g({i}) = {-3 * i ** 2 + 8 * i + 7}')

def main():
    equation.f()
    print('-' * 50)
    equation.g()


if __name__ == '__main__':
    main()