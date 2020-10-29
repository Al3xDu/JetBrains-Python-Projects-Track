from utils_printer import print_hi_to_this_project

import random


def main():
    list_of_words = ['python', 'java', 'kotlin', 'javascript']
    right_word = list(random.choice(list_of_words))
    array_of_chars = set(right_word)
    template_of_word = list('-' * len(right_word))
    i = 0
    while i < 8:
        print("\n" + ''.join(template_of_word))
        char = input("Input a letter: ")
        if char in array_of_chars:
            for k in range(len(right_word)):
                if right_word[k] == char:
                    template_of_word[k] = char
            if array_of_chars is not None:
                array_of_chars.remove(char)
        else:
            print("That letter doesn't appear in the word")
        i += 1
    print('''\nThanks for playing!
    We\'ll see how well you did in the next stage''')


if __name__ == '__main__':
    print_hi_to_this_project()
    main()
