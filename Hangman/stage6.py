def solve_sixth():
    import random

    word_list = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(word_list)
    life = 8
    dashed = "-" * len(word)
    print("H A N G M A N")
    dashed = list(dashed)
    mystery = ""
    status = ""
    game = True

    while game:
        if word == mystery.join(dashed):
            status = "You guessed the word!"
            game = False
        print()
        print(mystery.join(dashed))
        guess = input("Input a letter: ")
        if guess in word:
            if guess in dashed:
                life -= 1
                if life == 0:
                    status = "No improvements"
                    game = False
                elif life > 0:
                    status = "No improvements"
                print(status)
            elif word.count(guess) == 1:
                dashed[word.find(guess)] = guess
            elif word.count(guess) > 1:
                dashed[word.find(guess)] = guess
                dashed[word.rfind(guess)] = guess
        elif guess not in word:
            life -= 1
            if life == 0:
                status = "That letter doesn't appear in the word"
                game = False
            elif life > 0:
                status = "That letter doesn't appear in the word"
            print(status)
        if word == mystery.join(dashed):
            status = "You guessed the word!"
            game = False
    else:
        if life != 0:
            print("You survived!")
        else:
            print("You lost!")