from gtts import gTTS
import os

def readFromDatabase():
    global dictWords

    data=open("translate.txt")
    info=data.read().split("\n")

    dictWords=[]
    for i in range(0,len(info),2):
        myDictionry={"English":info[i],"Persian":info[i+1]}
        dictWords.append(myDictionry)


    data.close()

def showMenu():
    print("Here is the menu!!\n")
    print("1.Translate from english to persian")
    print("2-Translate from persian to english")
    print("3-Add new words")
    print("4-Exit")

def addNewWord():
    newEngWord = input("Enter your english word to be added to the dictionary: ").lower()
    
    for word in dictWords:
        if newEngWord == word["English"]:
            print("your word is already exists")
            print(word["English"], ":", word["Persian"] )
            break
    else:
        newPerWord = input("Enter the persian meaning of your entered word: ").lower()
        newWord = {"English":newEngWord, "Persian":newPerWord}
        dictWords.append(newWord)
        f = open("translate.txt", "a")
        f.write("\n")
        f.write(newEngWord)
        f.write("\n")
        f.write(newPerWord)
        f.close()
        print("you successfully add", newEngWord, ":", newPerWord, "to the dictionary")

def English_to_Persian():
    userText=input("please enter your english text:")
    userSentences=userText.split(".")
    for userSentence in userSentences: 
        userWords=userSentences.split(" ")
        translation=" "
        for userWord in userWords:
            for word in dictWords:
                if userWord==word["English"]:
                    translation=translation+word["Persian"]+" "
                    break
            else:
                translation=translation+userWord+" "

    print(translation)

def Persian_to_English():
    userText=input("please enter your persian text:")
    userSentences=userText.split(".")
    for userSentence in userSentences: 
        userWords=userSentences.split(" ")
        translation=" "
        for userWord in userWords:
            for word in dictWords:
                if userWord==word["Persian"]:
                    translation=translation+word["English"]+" "
                    break
            else:
                translation=translation+userWord+" "

    print(translation)
    audio=gTTS(text=translation,lang="en",slow=False)
    audio.save("audio.mp3")
    os.system("start audio.mp3")

readFromDatabase()
print("Welcome to the translator")
while True:
    showMenu()
    choice=int(input("Please enter your choice:"))

    if choice==1:
        English_to_Persian()
    elif choice==2:
        Persian_to_English()
    elif choice==3:
        addNewWord()
    elif choice==4:
        exit(0)