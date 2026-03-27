import random

def game():
    print("you are playing the game....")
    score = random.randint(1,62) # number mera 1 se 62 ke bich ka hoga
    # Fetch the hi score
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"Your score: {score}")
    if(score>hiscore):
        # write this to the hiscore.txt file
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score

game()