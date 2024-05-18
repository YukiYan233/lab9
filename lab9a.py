#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:29:03 2024

@author: yukiyan
"""

#YukiYan

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


class RockPaperScissors:
    def __init__(self, num_players=1):
        self.choices = ['rock', 'paper', 'scissors']
        self.num_players = num_players
        self.scores = {'Player Wins': 0, 'Computer Wins': 0, 'Ties': 0}    
        
    def get_user_choice(self):
        """Prompt user to pick rock, paper, or scissors."""
        choice = input("Pick one of rock, paper or scissors: ").lower()
        while choice not in self.choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            choice = input("Pick one of rock, paper or scissors: ").lower()
        return choice

    def get_computer_choice(self):
        """Randomly select a choice for the computer."""
        return random.choice(self.choices)

    def determine_winner(self, p1, p2):
        """Determine the winner of a round."""
        if p1 == p2:
            return "It's a tie!"
        elif (p1 == 'rock' and p2 == 'scissors') or \
             (p1 == 'scissors' and p2 == 'paper') or \
             (p1 == 'paper' and p2 == 'rock'):
            self.scores['Player Wins'] += 1
            return "Player wins!"
        else:
            self.scores['Computer Wins'] += 1
            return "Computer wins!"

    def play_round(self):
        """Play a single round of Rock-Paper-Scissors."""
        if self.num_players == 0:
            p1 = self.get_computer_choice()
            p2 = self.get_computer_choice()
        elif self.num_players == 1:
            p1 = self.get_user_choice()
            p2 = self.get_computer_choice()
        else:
            p1 = self.get_user_choice()
            p2 = self.get_user_choice()

        print(f"Player 1 chose {p1}, Player 2/Computer chose {p2}.")
        print(self.determine_winner(p1, p2))

    def play_game(self):
        """Control game playing multiple rounds until the user quits."""
        while True:
            self.play_round()
            print(f"Scores: {self.scores}")
            if input("Play another round? (yes/no): ").lower() != 'yes':
                break

def main():
    num_players = int(input("Enter the number of human players (0-2): "))
    while num_players not in [0, 1, 2]:
        print("Invalid number of players. Please enter 0, 1, or 2.")
        num_players = int(input("Enter the number of human players (0-2): "))
        
    game = RockPaperScissors(num_players)
    game.play_game()

if __name__ == "__main__":
    main()