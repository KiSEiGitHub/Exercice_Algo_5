def boucle(n):
    return sum(1 for _ in range(1, n))

def main():
    while True:
        n = int(input('n >> '))
        resultat_n = boucle(n)
        print(resultat_n)
        print('-' * 50)

if __name__ == '__main__':
    main()