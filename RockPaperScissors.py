from random import choice

class RockPaperScissors:
    """
    Represents a Rock, Paper, Scissors game between a user and a computer.
    """

    user_wins = 0
    computer_wins = 0
    max_rounds = 0
    rounds = 0
    answers = ['rock', 'paper', 'scissors']
    tie = "tie"

    def __init__(self, max_rounds: int = 3):
        """
        Initializes the game with the optional `max_rounds` parameter.

        Args:
            max_rounds (int, optional): Maximum number of rounds. Defaults to 3.
        """
        self.max_rounds = max_rounds
        self.tie = "tie"

    def add_user_win(self):
        """
        Increments the number of user wins.
        """
        self.user_wins += 1

    def add_computer_win(self):
        """
        Increments the number of computer wins.
        """
        self.computer_wins += 1

    def get_user_wins(self) -> int:
        """
        Returns the current number of user wins.

        Returns:
            int: The number of user wins.
        """
        return self.user_wins

    def get_computer_wins(self) -> int:
        """
        Returns the current number of computer wins.

        Returns:
            int: The number of computer wins.
        """
        return self.computer_wins

    def user_won(self, computer_answer: str, user_answer: str) -> bool | str:
        """
        Determines the winner of a round based on the user's and computer's answers.

        Args:
            computer_answer (str): The computer's answer.
            user_answer (str): The user's answer.

        Raises:
            ValueError: If either answer is invalid.

        Returns:
            bool | str: True if the user won, False if the computer won, or "tie" if it's a tie.
        """
        if computer_answer not in self.answers or user_answer not in self.answers:
            raise ValueError("User or computer answer is invalid.")

        if computer_answer == user_answer:
            return self.tie
        elif (computer_answer == "scissors" and user_answer == "rock" or
              computer_answer == "rock" and user_answer == "paper" or
              computer_answer == "paper" and user_answer == "scissors"):
            return True

        return False

    def check_rounds(self) -> bool:
        """
        Checks if the maximum number of rounds has been played.

        Returns:
            bool: True if there are rounds remaining, False otherwise.
        """
        return self.rounds < self.max_rounds

    def add_round(self):
        """
        Increments the current round number.
        """
        self.rounds += 1

    def get_round_count(self) -> int:
        """
        Returns the current round number.

        Returns:
            int: The current round number.
        """
        return self.rounds

    def get_computer_answer(self) -> str:
        """
        Generates and returns a random answer for the computer.

        Returns:
            str: A random answer from the list of valid options ("rock", "paper", or "scissors").
        """
        return choice(self.answers)
      
