print("Welcome to the Rock Paper Scissors game!")
print("You can choose either rock, paper or scissors.")
print("Rock beats scissors, scissors beats paper, paper beats rock.")
print("If you want to quit, just type 'quit'")
print("Let's start!")

score = 0
while True:
    player = input("enter your choice: rock, paper or scissors?").lower()
    if player == "quit":
        print("Thanks for playing!")
        print("Your score is: " + str(score))
        break
    if player not in ["rock", "paper", "scissors"]:
        print("Please enter a valid choice.")
        continue
    import random
    computer = random.choice(["rock", "paper", "scissors"])
    print("Computer chose: " + computer)
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("You win!")
        score += 1
    else:
        print("You lose!")
        score -= 1
    print("Your score is: " + str(score))
