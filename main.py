import adm.zmath
import main

in_action = 0


def print_main():
    print("1. Администратор")
    print("2. Кассир")
    main.in_action = int(input())


def do_main():
    while True:
        print_main()


if __name__ == '__main__':
    do_main()

