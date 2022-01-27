import random
plays = ["rock", "paper", "scissors"]

def computer_play():
    comp_play = plays[random.randint(0,2)]
    return comp_play

def human_play():
    while True:
        print("Choose rock, paper, or scissors.")
        human_play = input("One, two, three, shoot! ")
        if human_play not in plays:
            print("Not a valid play, try again.")
        else:
            return human_play

def find_winner():
    if comp_play == human_play:
        print(f"Computer picked {comp_play}, it's a tie.")
    elif (comp_play == "rock" and human_play == "paper")\
        or (comp_play == "scissors" and human_play == "rock")\
        or (comp_play == "paper" and human_play == "scissors"):
        print(f"Computer picked {comp_play}, you win.")
    else:
        print(f"Computer picked {comp_play}, you lose.")


comp_play = computer_play()
human_play = human_play()
find_winner()
print("bye")
