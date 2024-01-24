import random
from colorama import init
from colorama import Fore, Back, Style
from os import system, name
import time
from langdetect import detect



# Attachments section
label = """ __  __     ______     __  __     ______     ______     __  __     ______     __  __     __    
/\ \/ /    /\  __ \   /\ \/ /    /\  ___\   /\  ___\   /\ \/\ \   /\  == \   /\ \/\ \   /\ \   
\ \  _"-.  \ \  __ \  \ \  _"-.  \ \  __\   \ \ \__ \  \ \ \_\ \  \ \  __<   \ \ \_\ \  \ \ \  
 \ \_\ \_\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ 
  \/_/\/_/   \/_/\/_/   \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_/ /_/   \/_____/   \/_/ 
--The Rock-Paper-Scissors game--

"""
paper = [[';$$$$$$$$$$$$$$$$$$$$$$$$$$$;'],
         [';X            $:;          ;X'],
         [';X      .x+  .  X.         ;X'],
         [';X      ;  X .  X   ; .;   ;X'],
         [';  :;:  +  ; .  X  .+ .;   ;X'],
         [';  X :: +  ; +  X  ;  :    ;X'],
         [';  X  ; ;. + .  X :; .+    ;X'],
         [';  ;  :;;  : .  X +  +     ;X'],
         [';  .X  +:: ; .  +:; ;:     ;X'],
         [';   ;.  +           x  .;;  X'],
         [';X   +              . +: ;  X'],
         [';X   ;:           x:;. ;:   X'],
         [';X   X          .     :.   ;X'],
         [';X   X         :     ::    ;X'],
         [';X    ;.             ;     ;X'],
         [';X     .+:.;++;;++++.      ;X'],
         [';$$$$$$$$$$$$$$$$$$$$$$$$$$$;']]
scissors = [[';$$$$$$$$$$$$$$$$$$$$$$$$$$$;'],
            [';X         .+.+:           X:'],
            [';X         ;   ;.  .+ .+   X:'],
            [';X         +   .;  ;   +.  X:'],
            [';X         +.   +  X   ;.  X:'],
            [';X          ;   + .+   x   X:'],
            [';X          ;:  ; ::   X   X:'],
            [';X      :;XX++  :;:    ;   X:'],
            [';   .;.;    :. .::.   .:   X:'],
            [';  ::  X  +:::      ::X.   X:'],
            [';  ;.   ;  +::..:;+    ;:  X:'],
            [';  .x;. .;:   ;:+       ;  X:'],
            [';   + .;+.;;++::;      .;  X:'],
            [';X  :.          ;.     x   X:'],
            [';X  .+               .+    X:'],
            [';X    .++:.;++;;+++++.     X:'],
            [';$$$$$$$$$$$$$$$$$$$$$$$$$$$;']]
rock = [[';$$$$$$$$$$$$$$$$$$$$$$$$$$$;'],
        [';X                         X:'],
        [';X                         X:'],
        [';X          :X;:X:xX+.     X:'],
        [';X      +: X.    X    X.   X:'],
        [';     :.   ;.    +Xx+ ..   X:'],
        [';  x   .    x+:.      ;;   X:'],
        ['; ;    $   .;           +:  :'],
        ['; ;     ;   .x:    :+    :; :'],
        [';  +    ::   :; +         + :'],
        [';  .x+ ;:.:  ;;+         ;: :'],
        [';X  X          :        ::  :'],
        [';X  ::                 ;:  X:'],
        [';X   ;.               ;.   X:'],
        [';X    .X   ;+:   .;xX+     X:'],
        [';X                         X:'],
        [';$$$$$$$$$$$$$$$$$$$$$$$$$$$;']]
scroll = r"""                                             _______________________
   _______________________-------------------                       `\
 /:--__                                                              |
||< > |                                   ___________________________/
| \__/_________________-------------------                         |
|                                                                  |
 |               THE EPIC ROCK-PAPER-SCISSORS CHALLENGE             |
 |                                                                  |
 |          "Three symbols for the players' strategy,               |
  |        Rock to crush, Paper to cover, Scissors to cut,           |
  |      A dynamic game where strategies may swiftly change.         |
  |       Test your wits, master the throws,                          |
  |         One game to rule them all, in this thrilling encounter.  |
   |       In the arena where choices dance,                         |
   |       Rock, Paper, Scissors, a game of chance."                  |
   |                                                                  |
  |                                              ____________________|_
  |  ___________________-------------------------                      `\
  |/`--_                                                                 |
  ||[ ]||                                            ___________________/
   \===/___________________--------------------------
"""
controls = """Your controls:
C - to see controls again
Q - to quit the game completely
I - to see instructions
S - to see scroll
"""
instructions = """Overview:

1. Opponent:
    Face off against the computer in this "Kakegurui" version of Rock-Paper-Scissors game.
2. Card Deck:
    A deck of 30 random cards has been prepared for your gaming pleasure.
3. Chips and Currency:
    You start with 120 chips, each valued at $1,000 USD, for a total of $240,000 USD.
4. Endless Fun:
    Play as long as you wish, until you decide to cash out or your chips run dry.

Round Mechanics:

1. Card Distribution:
    At the beginning of each round, you and the computer receive 3 cards from the deck.
2. Round Resolution:
    Rounds continue until there's a clear winner.
    Ties lead to playing the remaining cards, progressing to the next round if necessary.
3. Your Decision:
    After each round, decide whether to continue or leave with your current chip count.
4. Get Ready to Be Surprised!
    Keep an eye out for exciting surprises as you progress through the game.

The End:

1. Game Outcome:
    If you're successful, you'll celebrate your victory in this exciting game.
2. Debt Settlement:
    If you face a loss, explore unique options to settle the debt:
        - Sell your soul to us.
        - Become a slave.
        - Sell your relatives.
"""


def detect_language(text):
    try:
        language = detect(text)
        return language
    except Exception as e:
        print(f"Error detecting language: {e}")
        return None

def clear():
    '''
    Это функция для очистки консоли
    '''
    # For Windows
    if name == 'nt':
        _ = system('cls')

    # For Mac and Linux
    else:
        _ = system('clear')

# ... (Previous code remains unchanged)

# Gameplay section
def play_round(player_cards, computer_cards):
    """
    Play a round of Rock-Paper-Scissors.

    Args:
    - player_cards (list): The player's cards for the current round.
    - computer_cards (list): The computer's cards for the current round.

    Returns:
    - result (str): The result of the round ('win', 'lose', or 'tie').
    """
    # Display available cards
    print("Your cards:", player_cards)
    print("Computer's cards:", computer_cards)

    # Get player's choice
    player_choice = input("Choose your move (Rock, Paper, or Scissors): ").lower()

    # Get computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine the winner
    result = determine_winner(player_choice, computer_choice)

    # Display the result
    print(f"You chose {player_choice.capitalize()}")
    print(f"Computer chose {computer_choice.capitalize()}")
    print(f"Result: {result.capitalize()}")

    return result


def determine_winner(player_choice, computer_choice):
    """
    Determine the winner of a Rock-Paper-Scissors round.

    Args:
    - player_choice (str): The player's choice ('rock', 'paper', or 'scissors').
    - computer_choice (str): The computer's choice ('rock', 'paper', or 'scissors').

    Returns:
    - result (str): The result of the round ('win', 'lose', or 'tie').
    """
    if player_choice == computer_choice:
        return "tie"
    elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "win"
    else:
        return "lose"


def main():
    # ... (Previous code remains unchanged)
    init(autoreset=True)

    clear()  # Очищаем экран
    print(label)  # Приветствуем игрока
    print("""Do you wanna start? 
              Choose an option:
              1 - Yes, I'm ready. Start the game.
              2 - Nope. Quit the game.
              """)  # Игроку предлагается выбор действий
    inp = input("Option: ")  # Игрок делает выбор
    if inp == "1":
        clear()  # Очищаем экран
        print(scroll)  # Выводим древний свиток
        print(controls)  # Вывод список с управлением в игре

        while True:
            inp = input("Press any key from controls (Tip: press 'C' for controls): ").upper()

            if inp == "Q":
                exit()  # Quit the game
            elif inp == "C":
                clear()
                print(controls)  # Display controls
            elif inp == "I":
                clear()
                print(instructions)  # Display instructions
            elif inp == "S":
                clear()
                print(scroll)  # Display scroll
            else:
                # Player selected an action, play a round
                player_cards = ["rock", "paper", "scissors"]
                computer_cards = ["rock", "paper", "scissors"]

                result = play_round(player_cards, computer_cards)

                # Handle result
                if result == "win":
                    print(Fore.GREEN + "You won this round!\n" + Fore.RESET)
                elif result == "lose":
                    print(Fore.RED + "You lost this round!\n" + Fore.RESET)
                else:
                    print("It's a tie! The round will continue.\n")
    else:
        return


if __name__ == "__main__":
    main()
