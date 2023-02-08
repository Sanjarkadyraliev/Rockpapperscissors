import random
choice = ['r', 'p', 's']
count = [0, 0]
def check_answer(t):
        if t == "r":
            print("rock")
        elif t == "p":
            print("paper")
        elif t == "s":
            print("scissors")

def main():
    while checkTotalScore():
        turn = input("Please enter your turn: ('r', 'p', 's'): ").lower()
        while turn not in choice:
            turn = input("Please enter your turn: ('r', 'p', 's'): ").lower()
        if turn == "exit":
            break
        else:
            check_answer(turn)
            c_turn = random.choice(choice)
            check_answer(c_turn)
            score(turn,c_turn)



def checkTotalScore():
    if count[0] == 3:
        return False
    if count[1] == 3:
        return False
    return True

def score (turn, c_turn):
    if turn == "r" and c_turn == "s" or turn == "p" and c_turn == "r" or turn == "s" and c_turn == "p":
        print("you win")
        count[0] += 1
    elif c_turn == "r" and turn == "s" or c_turn == "p" and turn == "r" or c_turn == "s" and turn == "p":
        print("comp win")
        count[1] += 1
    print("score:", *count)
    if turn == "r" and c_turn == "r" or turn == "p" and c_turn == "p" or turn == "s" and c_turn == "s":
        print("draw")

    if count[0] > count[1] and count[0] == 3:
        print("You win the game")
    if count[1] > count[0] and count[1] == 3:
        print("comp win the game")

def playAgain():
    options = ['YES', 'NO']
    response = input("Do you wanna play again:(yes or no): ").upper()
    while response not in options:
        response = input("Choose Yes or No: ").upper()
    if response =="YES":
        return True
    elif response == "NO":
        return False

def main_2():
    while playAgain():
        count[0] *= 0
        count[1] *= 0
        main()
    else:
        print("Bye !")


main()
main_2()