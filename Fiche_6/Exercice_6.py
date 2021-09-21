import random


def main():
    nb_mystere = random.randint(10, 100)
    print('Trouver le nombre entre 10 et 100')
    print('Vous avez 6 essaies')
    e = 6
    while True:
        print(f'{e} essaies restant')
        user = int(input('>> '))

        if user == nb_mystere:
            print('Vous avez trouvé !')
            break
        elif user < nb_mystere:
            print("C'est plus")
            e -= 1
            if e <= 0:
                print('Vous avez perdu !')
                break
        elif user > nb_mystere:
            print("C'est moins")
            e -= 1
            if e <= 0:
                print('Vous avez perdu !')
                break


if __name__ == '__main__':
    main()