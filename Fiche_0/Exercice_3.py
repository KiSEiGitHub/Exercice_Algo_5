def v(d, t):
    return d / t


def main():
    cycliste = v(80, 2.3)
    avion = v(2000, 3.45)
    voiture = v(490, 5.20)

    print(f'Vitesse cycliste = {round(cycliste, 2)} km/h')
    print(f'Vitesse avion = {round(avion, 2)} km/h')
    print(f'Vitesse voiture = {round(voiture, 2)} km/h')


if __name__ == '__main__':
    main()