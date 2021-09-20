class exo2:
    def __init__(self, a=0, m=0, n=0, a2=0, b=0):
        self.a = a
        self.m = m
        self.n = n
        self.a2 = a2
        self.b = b

    def algo_1(self):
        b = 6 * self.a
        c = self.a + b
        return b - c

    def algo_2(self):
        a = self.m * self.n
        b = self.m + self.n
        return a / b

    def algo_3(self):
        p = self.b ** self.a2
        q = p ** self.a2
        return p, q

def main():

    swtich = {
        '1': exo2,
        '2': exo2,
        '3': exo2
    }

    print('Algo 1 | 2 | 3')
    user = ""
    while user not in ['1', '2', '3']:
        user = input('>> ')

    if user == '1':
        a = int(input('A: '))
        fonc = swtich.get(user)
        print(fonc(a).algo_1())

    elif user == '2':
        m = int(input('m: '))
        n = int(input('n: '))
        fonc = swtich.get(user)
        print(fonc(m, n).algo_2())

    elif user == '3':
        a2 = int(input('a: '))
        b = int(input('b: '))
        fonc = swtich.get(user)
        print(fonc(a2, b).algo_3())



if __name__ == '__main__':
    main()