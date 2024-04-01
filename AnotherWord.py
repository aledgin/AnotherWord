#Another Word Game
#Inspired by "Wordle" and "Lingo."
#Code written by Alfred Ledgin

import random

#Make list of five-letter words.

print("Loading...")

#Need a text file listing words, each on a new line.
wordFile = open("words.txt", "r")
wordList = wordFile.readlines()
wordFile.close()

newWords = []      
for word in wordList:
    newWords.append(word.strip().upper())

##To test list of words:
#for i in range(5):
#    print(newWords[i])

#To ensure each word only has 5 letters, no more, no less.
validWords = []
for strippedWord in newWords:
    if len(strippedWord) == 5:
        validWords.append(strippedWord)
print(str(len(validWords)) + " words loaded.")
print("")

#Load high score.
highScore = 0
score = 0
try:
    scoreFile = open("score.txt", "r")
    loadedScore = int(scoreFile.read())
    highScore = loadedScore
    scoreFile.close()
except:
    highScore = 0

#Letter dictionary.
def getLetterDict(inputWord):
    letterDict = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0,
        'G': 0,
        'H': 0,
        'I': 0,
        'J': 0,
        'K': 0,
        'L': 0,
        'M': 0,
        'N': 0,
        'O': 0,
        'P': 0,
        'Q': 0,
        'R': 0,
        'S': 0,
        'T': 0,
        'U': 0,
        'V': 0,
        'W': 0,
        'X': 0,
        'Y': 0,
        'Z': 0
    }
    for i in range(len(inputWord)):
        letterDict[inputWord[i]] = letterDict[inputWord[i]] + 1
    return letterDict

#Game function.
def runGame():
    answer = random.choice(validWords)
    remainingGuesses = 6
    while remainingGuesses > 0:
        answerDict = getLetterDict(answer)
        print("Guess a 5-letter word")
        guess = input("->")
        guess = guess.upper()
        if guess in validWords:
            if guess == answer:
                print("[" + guess[0] + "]" + "[" + guess[1] + "]" + "[" + guess[2] + "]" + "[" + guess[3] + "]" + "[" + guess[4] + "]")
                print("Correct! The word is " + answer + ".")
                if remainingGuesses == 1:
                    print("You get " + str(remainingGuesses) + " point!")
                else:
                    print("You get " + str(remainingGuesses) + " points!")
                global score
                score = score + remainingGuesses
                return True
            else:
                #Game logic.
                for i in range(len(guess)):
                    if guess[i] == answer[i]:
                        answerDict[guess[i]] = answerDict[guess[i]] - 1
                resultString = ""
                for i in range(len(guess)):
                    if guess[i] == answer[i]:
                        resultString = resultString + "[" + guess[i] + "]"
                    elif answerDict[guess[i]] > 0:
                        resultString = resultString + "(" + guess[i] + ")"
                        answerDict[guess[i]] = answerDict[guess[i]] - 1
                    else:
                        resultString = resultString + "-" + guess[i] + "-"
                print(resultString)
                remainingGuesses = remainingGuesses - 1
                if remainingGuesses == 1:
                    print("You have " + str(remainingGuesses) + " more chance.")
                else:
                    print("You have " + str(remainingGuesses) + " more chances.")
        else:
            print("Word not found. Try again.")
    print("Sorry. The word is " + answer + ".")
    return False
        
#Run game.
isRunning = True
while isRunning == True:
    score = 0
    print("Welcome to Another Word Game")
    print("High Score: " + str(highScore))
    print("")
    print("You have 6 tries to guess a word.")
    print("Correct on 1st guess: 6 points")
    print("Correct on 2nd guess: 5 points")
    print("Correct on 3rd guess: 4 points")
    print("Correct on 4th guess: 3 points")
    print("Correct on 5th guess: 2 points")
    print("Correct on 6th guess: 1 point")
    print("")
    print("Key:")
    print("-X-    Letter is not in word")
    print("(X)    Letter is in word but in wrong place")
    print("[X]    Letter is in correct place")
    print("")
    print("Type 's' and press ENTER to Start.")
    print("Type 'e' and press ENTER to Exit.")
    theInput = input("->")
    if theInput == 'e':
        isRunning = False
        break
    elif theInput == 's':
        isPlaying = True
    else:
        print("Invalid input.")
        print("")
        continue

    hasNotLost = True
    while hasNotLost == True:
        print("")
        hasNotLost = runGame()
        print("Score: " + str(score))
        if hasNotLost == False:
            print("")
            break
        print("Another round awaits!")
        print("Press ENTER to continue, or enter the letter 'q' to quit.")
        anotherRound = input("->")
        if anotherRound == 'q':
            hasNotLost = False
            print("End of game. Your total score is " + str(score) + " points.")
            print("")
        else:
            hasNotLost = True

    if score > highScore:
        highScore = score
    
scoreFile = open("score.txt", "w")
scoreFile.write(str(highScore))
scoreFile.close()
