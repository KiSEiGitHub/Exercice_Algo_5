class solde:
    def __init__(self, prix, reduction):
        self.prix = prix
        self.reduc = reduction

    def calcul_nouveau_prix(self):
        price = self.prix * self.reduc / 100
        return self.prix - price

    def affich(self):
        print(f'Prix a payer: {round(self.calcul_nouveau_prix(), 2)} €')
        print('-' * 50)

def main():
    while True:
        try:
            base_prix = float(input('prix de base: '))
            redu = float(input('Réduction: '))
            c = solde(base_prix, redu)
            c.affich()
        except ZeroDivisionError:
            print('pas de 0')
        except ValueError:
            print('un nombre !')


if __name__ == '__main__':
    main()