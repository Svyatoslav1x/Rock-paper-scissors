import random
from collections import Counter

# Define the cards
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


def computer_move(player_moves):
    if player_moves:
        most_common_move = Counter(player_moves).most_common(1)[0][0]
        return beat(most_common_move)
    else:
        return random.choice(list(cards.keys()))


def beat(move):
    if move == 'Rock':
        return 'Paper'
    elif move == 'Paper':
        return 'Scissors'
    else:
        return 'Rock'


# Add the game logic to your main function
def main():
    # Your existing code here...

    # Define the box
    box = [random.choice(list(cards.keys())) for _ in range(30)]

    # Define the chips
    chips = 120

    # Initialize the game variables
    player_moves = []
    computer_moves = []

    # Game loop
    while True:
        # Round setup
        player_card = random.choice(box)
        computer_card = computer_move(player_moves)

        # Show the cards
        print("Your card:\n" + cards[player_card])
        print("Computer's card:\n" + cards[computer_card])

        # Round progress
        if beat(player_card) == computer_card:
            # Computer wins
            chips -= 1
        elif beat(computer_card) == player_card:
            # Player wins
            chips += 1

        # Update the moves
        player_moves.append(player_card)
        computer_moves.append(computer_card)

        # Player decision
        inp = input("Do you want to continue playing? (Y/N)").upper()
        if inp != 'Y':
            break

    # Super game option
    inp = input("Do you want to play the super game? (Y/N)").upper()
    if inp == 'Y':
        # Super game
        player_card = random.choice(box)
        computer_card = computer_move(player_moves)

        # Show the cards
        print("Your card:\n" + cards[player_card])
        print("Computer's card:\n" + cards[computer_card])

        if beat(player_card) == computer_card:
            # Computer wins
            chips -= 10000
        elif beat(computer_card) == player_card:
            # Player wins
            chips += 10000

    # End of the game
    if chips < 0:
        print("You lost the game. You need to settle the debt.")
    else:
        print("Congratulations! You won the game.")


if __name__ == "__main__":
    main()
