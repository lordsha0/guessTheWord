#! /usr/bin/python3

chosenWord = "Krasivaya"
wordIsFound = False

print("We have chosen a word, it's up to you to uncover it!")
while(not(wordIsFound)):
	print("Guess it!")
	userWord = input()
	if(userWord == chosenWord):
		wordIsFound = True
		print("Congrats, you found it!")
	else:
                nbLettersCorrect = 0
                if(len(userWord) == len(chosenWord)):
                    for i in range(0,len(userWord)):
                        if(userWord[i] == chosenWord[i]):
                            nbLettersCorrect += 1
                    print(f"Wrong word but you have {nbLettersCorrect} correct letters!")
                elif(len(userWord) < len(chosenWord)):
                    print("Your word is too short...")
                else:
                    print("Your word is too long...")
                print("Try again!")
