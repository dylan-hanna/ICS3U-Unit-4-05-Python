#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Oct 2019
# This program uses a for loop

def main():
    while True:
        try:
            total_numbers = []

            number = int(input("How many numbers do you want to add?: "))
            print()

            for addition in range(number):
                numbers = int(input("Enter a number to add: "))

                if numbers < 0:
                    continue

                total_numbers.append(numbers)

            print()
            print("Sum of numbers is =", sum(total_numbers))
            print("We excluded negatives becuase they aren't nice.")

        except ValueError:
            print()
            print("Not a number. I want an integer, like 4 or 67.")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()