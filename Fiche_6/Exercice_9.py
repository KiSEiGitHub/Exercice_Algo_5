import random


def main():
    t = []

    for _ in range(50):
        a = random.randint(1, 1000)
        t.append(a)

    print(f'total = {sum(t)}')


if __name__ == '__main__':
    main()