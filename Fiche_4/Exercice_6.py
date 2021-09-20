def main():
    a = float(input('prix total >> '))
    base = a * 5 / 100 if a <= 75 else a * 8 / 100
    prix_payer = a - base
    print(f'Prix a payer: {round(prix_payer, 2)} €')


if __name__ == '__main__':
    main()