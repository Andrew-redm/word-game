import random

def get_word(topic):
    words = {
        'animals': ['elephant', 'giraffe', 'kangaroo', 'dolphin'],
        'fruits': ['apple', 'banana', 'cherry', 'date'],
        'countries': ['canada', 'brazil', 'france', 'germany']
    }
    return random.choice(words[topic])

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def play_game(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def main():
    topics = ['animals', 'fruits', 'countries']
    print("Welcome to Hangman!")
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    if difficulty == 'easy':
        tries = 10
    elif difficulty == 'medium':
        tries = 6
    else:
        tries = 4

    print("Available topics:", topics)
    user_veto = input("Do you want to veto a topic? (yes/no): ").lower()
    if user_veto == 'yes':
        veto_topic = input("Which topic do you want to veto? ").lower()
        if veto_topic in topics:
            topics.remove(veto_topic)
    
    computer_veto = random.choice(topics)
    print(f"Computer vetoed the topic: {computer_veto}")
    topics.remove(computer_veto)

    print("Remaining topics:", topics)
    chosen_topic = random.choice(topics)
    print(f"Chosen topic: {chosen_topic}")

    word = get_word(chosen_topic)
    play_game(word)

if __name__ == "__main__":
    main()