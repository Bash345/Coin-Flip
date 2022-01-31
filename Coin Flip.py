import random

def coinFlip():
    flip = random.uniform(0,1)

    if flip > 0.5:
        print("True")
    else:
        print("False")

#run(1)