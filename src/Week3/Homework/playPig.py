import random

def playNextRound(playerScore):
    WINNING_SCORE = 100

    option = input("Roll dice (y/n)?").lower()
    while not (option == 'y' or option == 'n'):
                option = input("Please enter a valid option (y/n)?").lower()

    currentScore = playerScore

    while option == "y":
        diceRoll = random.randint(1, 6)

        if diceRoll == 1:
            print("You rolled 1!")
            break

        currentScore += diceRoll

        if currentScore >= WINNING_SCORE:
            print("Current Score: ", currentScore, end="\n")
            print("Congratulations, you've won!")
            return -1
        else:
            print("Current Score: ", currentScore, end="\n")
            option = input("Roll again (y/n)?").lower()

            while not (option == 'y' or option == 'n'):
                option = input("Please enter a valid option (y/n)?").lower()

    return currentScore

def playPig():
    scoreA = 0
    scoreB = 0
    currentPlayer = "Player A"

    while True:
        print("\n" + currentPlayer)

        if currentPlayer == "Player A":
            scoreA = playNextRound(scoreA)
            currentScore = scoreA
        else:
            scoreB = playNextRound(scoreB)
            currentScore = scoreB

        if currentScore == -1 :
            break
        elif currentPlayer == "Player A":
            currentPlayer = "Player B"
        else:
            currentPlayer = "Player A"

    return 0

playPig()