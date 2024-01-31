from colorama import init
from colorama import Fore, Back, Style
from os import system, name
import time
import random
from collections import Counter

# Attachments section
label = """ __  __     ______     __  __     ______     ______     __  __     ______     __  __     __    
/\ \/ /    /\  __ \   /\ \/ /    /\  ___\   /\  ___\   /\ \/\ \   /\  == \   /\ \/\ \   /\ \   
\ \  _"-.  \ \  __ \  \ \  _"-.  \ \  __\   \ \ \__ \  \ \ \_\ \  \ \  __<   \ \ \_\ \  \ \ \  
 \ \_\ \_\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ 
  \/_/\/_/   \/_/\/_/   \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_/ /_/   \/_____/   \/_/ 
--The Rock-Paper-Scissors game--

"""
cards = {
    'Rock': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    'Paper': """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """,
    'Scissors': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
}
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
instructions = """ 
Overview:

1. Opponent:
    Face off against the computer in this "Kakegurui" version of Rock-Paper-Scissors game.
2. Card Deck:
    A deck of 30 random cards has been prepared for your gaming pleasure.
3. Chips and Currency:
    You start with 120 chips, each valued at $1,000 USD. 
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
"""
nums = {
    1: """
  /$$  
 /$$$$  
|_  $$  
  | $$  
  | $$  
  | $$  
 /$$$$$$
|______/""",
    2: """
  /$$$$$$ 
 /$$__  $$
|__/  \ $$
  /$$$$$$/
 /$$____/ 
| $$      
| $$$$$$$$
|________/""",
    3: """
  /$$$$$$ 
 /$$__  $$
|__/  \ $$
   /$$$$$/
  |___  $$
 /$$  \ $$
|  $$$$$$/
 \______/ """
}
chips = 0
pc_chips = 120
if_supr_game_round_played = False
player_moves = []  # Определяем список для хранения ходов игрока


def computer_move(player_moves):
    # Функция описывает алгоритм хода пк
    if player_moves:  # Если это не первый раунд, то
        most_common_move = Counter(player_moves).most_common(1)[0][
            0]  # Выбиаем карту, которую игрок использует чаще всего
        return beat(most_common_move)  # Бьем эту карту
    else:
        return random.choice(list(cards.keys()))  # Возвращаем рандомную карту


def beat(move):
    # Функция возвращает карту для победы против move
    if move == 'Rock':
        return 'Paper'
    elif move == 'Paper':
        return 'Scissors'
    else:
        return 'Rock'


def print_stats():
    print(f"""Stats:
          chips -- {chips} 
          opponent's chips -- {pc_chips} 
          """)


def play_super_game():
    '''
    Это функция для SUPER game. (Супер режим, ну знаете, ох уж этот супер режим для последнего раунда)
    '''
    global chips  # Хотим менять глобальные переменные
    global pc_chips
    clear()  # Очищаем экран
    print("SUPER GAME starts!")
    print("You have only one chance!")

    while True:  # Заставляем ввести карту
        print("Enter 'Rock', 'Paper' or 'Scissors'")
        player_card = input("Your card: ").capitalize()
        if (player_card == "Rock" or player_card == "Paper" or player_card == "Scissors"):
            break
    computer_card = computer_move(player_moves)  # Пк делает свой ход
    while computer_card == player_card:
        computer_card = computer_move(player_moves) # Добиваемся того, чтобы не было ничьи
    clear()  # Очищаем экран
    # Выводим ходы игроков
    print("Your card:\n" + cards[player_card])
    print("Computer's card:\n" + cards[computer_card])

    # Определяем победителя
    if beat(player_card) == computer_card:
        # Выиграл пк
        chips -= 1000000
        print("You lost!")
        print("-1.000.000")
    elif beat(computer_card) == player_card:
        # Выиграл игрок
        chips += 1000000
        print("You win!")
        print("+1.000.000")
    
    inp = input("Press any key to continue: ")
    return

        
        

def play_the_game():
    '''
    Это функция для разыгрывания раунда
    '''
    clear()  # Очищаем экран
    print(
        "Enter '1' to enter the bet or press 'C' to see stats")  # Просим игрока ввести ставку для этого раунда
    while True:  # Запускаем цикл разыгрывания раунда
        inp_pl_dec = input("Your choice (C): ").lower()  # Игрок вводит одну из опций
        if (inp_pl_dec == ""):
            print_stats()  # Выводим статы
        elif (inp_pl_dec == "1"):
            global chips  # Хотим менять глобальные переменные
            global pc_chips

            clear()  # Очищаем экран
            print("Enter the amount you want to bet on the round")  # Просим игрока ввести ставку для этого раунда
            print_stats()  # Выводим статы

            inp_bet = int(input("Your bet: "))  # Игрок вводит ставку
            if (inp_bet > chips):
                while inp_bet > chips:  # Заставляем игрока ввести число для ставки меньшее чем его число фишек
                    print("You don't have enough chips!")
                    inp_bet = int(input("Your bet: "))

            pc_bet = random.randrange(pc_chips + 1)  # Ставка пк для раунда определяется рандомно

            tmp_chips = chips  # Делаем дампы фишек игроков
            tmp_pc_chips = pc_chips
            chips -= inp_bet  # До оканчания раунда фишки игроков отправляются в общий банк
            pc_chips -= pc_bet

            total_bet = pc_bet + inp_bet  # Составляем общий банк для раунда

            clear()
            print(f"\tYour bet: {inp_bet}")
            print(f"\tOpponent's bet: {pc_bet}")
            print(f"\tTotal bet: {total_bet}")  # Выводим общий банк
            while True:  # Заставляем ввести карту
                print("Enter 'Rock', 'Paper' or 'Scissors'")
                player_card = input("Your card: ").capitalize()
                if (player_card == "Rock" or player_card == "Paper" or player_card == "Scissors"):
                    break
            computer_card = computer_move(player_moves)  # Пк делает свой ход

            clear()  # Очищаем экран
            # Выводим ходы игроков
            print("Your card:\n" + cards[player_card])
            print("Computer's card:\n" + cards[computer_card])

            # Определяем победителя
            if beat(player_card) == computer_card:
                # Выиграл пк
                pc_chips += total_bet
                print("You lost!")
                print(f"-{inp_bet}")
            elif beat(computer_card) == player_card:
                # Выиграл игрок
                chips += total_bet
                print("You win!")
                print(f"+{pc_bet}")
            else:
                # Ничья
                print("Draw!")
                pc_chips = tmp_pc_chips
                chips = tmp_chips

            player_moves.append(player_card)  # Обновляем список ходов игрока
            inp = input("Press any key to continue: ")
            return


def play_rounds():
    '''
    Это основная функция для раундов в игре. Здесь определяется победитель, кол-во фишек и т.д.
    '''

    clear()  # Очищаем экран перед раундом
    print_stats()  # Выводим кол-во фишек игрока и пк
    if (chips <= 0):
        print("You can't play the regular round. But you can play SUPER GAME.")

        while True:  # Заставляем игрока ввести или Enter или "Y"
            inp_pl_dec = input("Do you want to play SUPER GAME (N/y): ").lower()
            if (inp_pl_dec == "y"):  # Игрок согласился на супер игру
                play_super_game()  # Начинаем супер игру, после этой строки игра завершается
                if chips > 0:
                    print("You are the winner! Congratulations!")
                    print(f"Here are your chips: {chips}. You can take them")
                else:
                    print("You've lost everything.")
                    time.sleep(0.5)
                    print("It's time to pay the debts")
                    time.sleep(0.5)
                    print("Check your device register)")
                exit()
            elif (inp_pl_dec == ""):
                return
            else:
                print("Press 'Enter' or 'y'!")  # Просим ввести нужные нам данные для продолжения алгоритма
    else:
        opt_list = """Do you wanna start? 
          Choose an option:
          1 - Yes, I'm ready. Start the round.
          2 - Nope. Quit the round.
          """
        print(opt_list)  # Игроку предлагается выбор действий
        while True:
            inp = input("Option: ")  # Заставляем ввести нужные нам данные для продолжения алгоритма
            if (inp == "1"):
                play_the_game()
                return
            elif (inp == "2"):
                print("Quiting the round...")
                time.sleep(1.5)
                return


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
    chips -- фишки игрока
    pc_chips -- фишки пк
    nums -- словарь ASCII цифр
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
        controls = """Your controls:
        1 - start the round
        C - to see controls again
        Q - to quit the game completely
        I - to see instructions
        S - to see scroll
        E - to see your stats
        """
        clear()  # Очищаем экран
        print(scroll)  # Выводим древний свиток
        print(controls)  # Вывод список с управлением в игре

        while True:  # Начинаем основной цикл игры
            inp = input("Press any key from controls (C): ").upper()
            if (inp == "Q"):
                if chips > 0:
                    print("You are the winner! Congratulations!")
                    print(f"Here are your chips: {chips}. You can take them")
                else:
                    print(f"You've lost {-1 * chips}")
                    print("You have to pay your debts")
                inp = input("Press any key to continue: ")
                exit()  # Выходим из игры
            elif (inp == "C" or inp == ""):
                clear()
                print(controls)  # Вывод список с управлением в игре
            elif (inp == "I"):
                clear()
                print(instructions)  # Ознакамливаем игрока с правилами игры
            elif (inp == "S"):
                clear()
                print(scroll)  # Выводим древний свиток
            elif (inp == "1"):
                clear()
                print("You've started the round")
                print("Don't touch your keyboard!")
                for i in range(3):  # Start counting
                    time.sleep(1)  # Wait before printing
                    clear()  # Clear the screen
                    print(nums[i + 1])  # Print num
                time.sleep(1)  # Wait before round
                play_rounds()  # Start the round
                clear()
                print(controls)
            elif (inp == "E"):
                print_stats()  # Выводим статы


    else:
        exit()


if __name__ == "__main__":
    main()
