import threading as th
import os
import json
import random
import time

class cliType():
    def __init__(self,words):
        self.correct_words=0
        self.all_words=0
        self.mainMenu(words)

    def calculateAccuracy(self):
        self.acc_calculation=(self.correct_words/self.all_words)*100
        return self.acc_calculation

    def finished(self):
        print("")
        print("-"*50)
        print("Done!")
        print("%s Words Per Minute" %self.correct_words)
        self.calculateAccuracy()
        print("Accuracy : {:.2f} %".format(self.acc_calculation))
        os._exit(0)

    def typingTest(self,words):
        print()
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("")
        print("START!")
        print("-"*50)
        extTimer=th.Timer(60.0,self.finished)
        extTimer.start() 
        while True:
            for word in range(0,len(words)):
                print("")
                print(words[word])
                user=input("Type : ").lower()
                if(user==words[word]):
                    self.correct_words+=1
                else:pass
                self.all_words+=1

    def mainMenu(self,words):
        print()
        print("CLI TYPING SPEEDZ TEZT 1000 BY EDZ")
        print("-"*50)
        print("You have 1 minute to type the random words given by the computer!")
        print("Press 0 to quit")
        print("Press 1 to play")
        print("")
        user=int(input("Answer : "))
        if user==0:
            print("")
            print("Aye sir!")
            exit()
        elif user==1:
            self.typingTest(words)                    

if __name__=="__main__":
    wordsDisplay=[]
    with open("words.json","r") as f:
        data=json.load(f)
    while len(wordsDisplay)<=100:
        wordsDisplay.append(random.choice(data["words"]))
    app=cliType(wordsDisplay)
    app()