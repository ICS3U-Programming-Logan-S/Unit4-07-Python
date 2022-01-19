# Created by: Logan S
# Created on: Jan 19, 2022
# This program prints numbers in lines of 5 from 1000 to 2000.

def main():
    # this function is the the Fizz-Buzz problem

    for counter in range(1000, 2001, 1):
        if counter % 5 == 0:
            print()
        print(counter, " ", end="")


if __name__ == "__main__":
    main()
