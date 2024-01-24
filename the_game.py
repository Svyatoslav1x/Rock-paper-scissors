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


# Gameplay section
def main():
    '''
    Основная функция программы.

    label -- название игры
    paper -- карточка с бумагой
    scissors -- карточка с ножницами
    rock -- карточка с камнем
    scroll -- свиток с описанием игры
    controls -- список с клавишами для управлении игрой
    instructions -- инструкция для игры
    '''

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
        while True:  # Начинаем основной цикл игры
            inp = input("Press any key from controls('C'): ").upper()
            if (inp == "Q"):
                exit()  # Выходим из игры
            elif (inp == "C"):
                clear()
                print(controls)  # Вывод список с управлением в игре
            elif (inp == "I"):
                clear()
                print(instructions)  # Ознакамливаем игрока с правилами игры
            elif (inp == "S"):
                clear()
                print(scroll)  # Выводим свиток
    else:
        exit()


if __name__ == "__main__":
    main()
