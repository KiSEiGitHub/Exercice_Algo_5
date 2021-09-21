def capital(capital, taux):
    a = 0
    somme = 0
    while somme <= capital * 2:
        somme += capital * taux / 100
        a += 1

    return a


def main():
    while True:
        cap = float(input('capital >> '))
        to = float(input('Taux >> '))
        annee = capital(cap, to)
        print(f'La somme aura doublé en {annee} ans')
        print('-' * 50)


if __name__ == '__main__':
    main()