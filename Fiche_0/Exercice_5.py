class triangle:
    def __init__(self, AB, BC, AC):
        self.AB = AB
        self.BC = BC
        self.AC = AC

    def rectangle(self):
        return self.AB ** 2 + self.BC ** 2 == self.AC ** 2

def main():
    a = triangle(4, 4, 8)
    print(a.rectangle())


if __name__ == '__main__':
    main()