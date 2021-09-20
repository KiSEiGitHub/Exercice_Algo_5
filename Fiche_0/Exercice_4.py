class division:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reste(self):
        return self.x % self.y

    def quotient(self):
        return self.x // self.y

    def print(self):
        print(f'division de {self.x} / {self.y}')
        print(f'Reste = {self.reste()}')
        print(f'Quotient = {self.quotient()}')
        print('-' * 50)

def main():
    while True:
        try:
            a = int(input('nombre: '))
            b = int(input('nombre: '))
            c = division(a, b)
            c.print()
        except ValueError:
            print('un nombre!')


if __name__ == '__main__':
    main()