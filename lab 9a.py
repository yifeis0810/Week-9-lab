#Yifei Su

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

class Player:
    def __init__(self, is_human=True):
        self.is_human = is_human

    def get_choice(self):
        if self.is_human:
            choice = input('Pick one of rock, paper, or scissors: ')
            while choice not in ['rock', 'paper', 'scissors']:
                print("Invalid choice. Please choose again.")
                choice = input('Pick one of rock, paper, or scissors: ')
            return choice
        else:
            return random.choice(['rock', 'paper', 'scissors'])

class Game:
    def __init__(self, num_human_players=1):
        self.players = [Player(i < num_human_players) for i in range(2)]
        self.results = {"wins": 0, "losses": 0, "draws": 0}

    determine_winner = lambda self, p1, p2: "draws" if p1 == p2 else (
        "wins" if (p1 == 'rock' and p2 == 'scissors') or 
                     (p1 == 'scissors' and p2 == 'paper') or 
                     (p1 == 'paper' and p2 == 'rock') else "losses")

    def play_round(self):
        p1_choice = self.players[0].get_choice()
        p2_choice = self.players[1].get_choice()
        print(f"Player 1 chose {p1_choice}, Player 2 chose {p2_choice}")

        result = self.determine_winner(p1_choice, p2_choice)
        self.results[result] += 1
        return f"Result: {result.capitalize()}!"

    def play_game(self, rounds=1):
        for _ in range(rounds):
            print(self.play_round())
        print("\nGame Summary:")
        print(f"Wins: {self.results['wins']}, Losses: {self.results['losses']}, Draws: {self.results['draws']}")

def main():
    num_players = int(input("Enter the number of human players (0, 1, or 2): "))
    while num_players not in [0, 1, 2]:
        print("Invalid number of players. Please enter 0, 1, or 2.")
        num_players = int(input("Enter the number of human players (0, 1, or 2): "))

    num_rounds = int(input("Enter the number of rounds to play: "))
    game = Game(num_human_players=num_players)
    game.play_game(rounds=num_rounds)

if __name__ == "__main__":
    main()


