import random

variants = ["stone", "scissor", "paper"]

player = input("Enter stone, scissor, or paper: ").lower()

if player not in variants:
    print("Invalid choice!")
else:
    pc = random.choice(variants)
    print(f"Computer chose: {pc}")

    if player == pc:

        print("Draw!")

    elif (player == "stone" and pc == "scissor") or \
         (player == "scissor" and pc == "paper") or \
         (player == "paper" and pc == "stone"):
        print("You win!")
    
    else:
        print("Computer wins!")