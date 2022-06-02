import random
user_wins = 0
computer_win = 0
rps = ["rock", "paper", "scissors"]

while True:
    user_play = input(
        "Welcome to the game click R for rock, P for paper and S for scissors: \n")
    if user_play not in rps:
        print("Invalid option!!")
        continue
    random_number = random.randint(0, 2)
    computer_play = rps[random_number]

    if user_play == "paper" and computer_play == "rock":
        print(f"You chose: {user_play}, Computer chose: {computer_play}")
        print("You win")
        user_wins += 1
        break
    elif user_play == "scissors" and computer_play == "paper":
        print(f"You chose: {user_play}, Computer chose: {computer_play}")
        print("You win")
        user_wins += 1
        break

    elif user_play == "rock" and computer_play == "scissors":
        print(f"You chose: {user_play}, Computer chose: {computer_play}")
        print("You win")
        user_wins += 1
        break

    elif user_play == computer_play:
        print(f"You chose: {user_play}, Computer chose: {computer_play}")
        print("Tie!")
        continue

    else:
        print(f"You chose: {user_play}, Computer chose: {computer_play}")
        print("You lost, computer wins")
        computer_win += 1
        break
print(
    f"Game Over, you won {user_wins} times computer won {computer_win} times")
