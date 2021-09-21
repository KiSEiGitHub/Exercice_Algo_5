import random


def main():
    s = 25
    d = 0
    while s <= 50:
        a = random.randint(1, 2)
        s += 1
        d += 1
        print(a)
    print(d - 1)


if __name__ == '__main__':
    main()