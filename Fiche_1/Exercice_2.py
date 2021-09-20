class remise:
    def __init__(self, prix, pourcentage):
        self.p = prix
        self.pourcentage = pourcentage

    def formule_remise(self):
        return self.p * self.pourcentage / 100

    def formule_prix_a_payer(self):
        base = self.p * self.pourcentage / 100
        return self.p - base

    def print(self):
        print(f'Prix de la remise = {self.formule_remise()} €')
        print(f'Prix a payer = {self.formule_prix_a_payer()} €')
        print('-' * 50)

def main():
    while True:
        b = float(input('prix: '))
        c = float(input('remise: '))
        z = remise(b, c)
        z.print()


if __name__ == '__main__':
    main()