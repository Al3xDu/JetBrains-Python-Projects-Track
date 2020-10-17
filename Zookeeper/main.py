from Zookeeper import animal_printer as pr
import sys


def main():
    while True:
        print("Please enter the number of the habitat you would like to view:")
        habitat_number = input()
        if habitat_number == "exit":
            print("See you later!")
            sys.exit(0)
        print(pr.animal_list[int(habitat_number)])
        print("---")
        print("You've reached the end of the program. To check another habitat, please restart the watcher.")


if __name__ == '__main__':
    main()
