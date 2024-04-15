import RockPaperScissors
import os

RPS = RockPaperScissors.RockPaperScissors(3)

while RPS.check_rounds():
  user_answer = input("Please enter an answer:\n> ").lower()
  computer_answer = RPS.get_computer_answer()
  RPS.add_round()
  os.system("clear")

  result = RPS.user_won(computer_answer, user_answer)
  if result == RPS.tie:
    print("Tie!")
    continue
  elif result:
    RPS.add_user_win()
    print("You won the round!")
    continue

  print("You lost the round!")
  RPS.add_computer_win()

def main():
  if RPS.user_wins == RPS.computer_wins:
    print("Tie!")
    return
  print(f"You {'won' if (RPS.user_wins > RPS.computer_wins) else 'lost'} the match!")
  
