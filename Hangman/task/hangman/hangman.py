import random
print("H A N G M A N")
while input('Type "play" to play the game, "exit" to quit: ') == "play":
    language = ['python', 'java', 'kotlin', 'javascript']
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = []
    word = random.choice(language)
    new_word = "-" * len(word)
    attempts = 8
    while new_word.count("-") and attempts != 0:
        print()
        print(new_word)
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should print a single letter")
        elif alphabet.count(letter) == 0:
            print("It is not an ASCII lowercase letter")
        elif answer.count(letter):
            print("You already typed this letter")
        elif word.count(letter) and letter == "a":
            new_word = new_word[:word.find(letter)] + letter + new_word[word.find(letter) + 1:word.rfind(letter)] + letter + new_word[word.rfind(letter) + 1:]
            print(new_word)
        elif word.count(letter):
            new_word = new_word[:word.find(letter)] + letter + new_word[word.find(letter) + 1:]
            print(new_word)
        else:
            print("No such letter in the word")
            attempts -= 1
        answer.append(letter)
    if attempts != 0:
        print("You guessed the word!\nYou survived!")
    else:
        print("You are hanged!")
    print()