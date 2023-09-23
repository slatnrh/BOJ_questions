def great_rich():
    money, life = input().split()
    money = int(money);
    life = int(life);

    print(money//life)
    print(money%life)


def main():
    great_rich()
main()