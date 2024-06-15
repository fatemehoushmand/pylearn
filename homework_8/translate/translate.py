# print (" TRANSLATOR ")

# from colorama import Fore
# import gtts

# def read_from_file () :
#     global WORDS_BANK

#     f = open ("translate.txt", "r")
#     WORDS_BANK = []

#     file = f.read ()
#     words = file.split ( "\n" )
#     for i in range ( 0 , len(words) , 2 ) :
#         dictionary = { "en" : words [i] , "fa" : words [i + 1]}
#         WORDS_BANK.append ( dictionary )

#     f.close ()


# def show_menue () :
#     print ("")
#     print ("                 menue                   ")
#     print (" print 1 to translate english to persian ")
#     print (" print 2 to translate persian to english ")
#     print (" print 3 to add a new word to words bank ")
#     print (" print 4 to exit ")
#     print ("")


# def english_to_persian () :
#     english = input (" Please enter your english text : ")
#     english_words = english.split (" ")
#     persian = ""
    
#     for word in english_words :
#         for existence in WORDS_BANK :
#             if word == existence["en"] :
#                 persian = persian + existence["fa"] + " "
#                 break
        
#         else :
#             persian = persian + word + " "

#     print ( Fore.CYAN , persian , Fore.RESET )


# def persian_to_english () :
#     persian = input (" Please enter your persian text in finglish writing : ")
#     persian_words = persian.split (" ")
#     english = ""

#     for word in persian_words :
#         for existence in WORDS_BANK :
#             if word == existence["fa"] :
#                 english = english + existence["en"] + " "
#                 break

#         else :
#             english = english + word + " "

    
#     print ( Fore.CYAN , english , Fore.RESET )
#     voice = gtts.gTTS ( english , lang = "en" , slow = False )
#     voice.save ("voice.mp3")


# def add () :
#     english = input (" Please enter the word in enlish : ")
#     persian = input (" Please enter the word in persian : ")
#     for word in WORDS_BANK :
#         if word["en"] == english or word["fa"] == persian :
#             print (" We have this word in word bank ")
#             break

#     else :
#         print (" Thank you for adding new word too my word band ")
#         new_word = { "en" : english , "fa" : persian }
#         WORDS_BANK.append ( new_word )


# def save_to_file () :
#     f = open ("translate.txt" , "w")
#     for word in WORDS_BANK :
#         f.write ( word["en"] + "\n" )
#         f.write ( word["fa"] + "\n" )
    
#     f.write ("\n")
#     f.close ()


# print (" Welcom to my translator ")  
# print (Fore.BLUE , "!! Please use space after all words and punctuation when you are entering a text for translastion !! " , Fore.RESET )
# print (Fore.BLUE , "!! Please use an underline '_' between two part words !! " , Fore.RESET )
# read_from_file ()

# while True :
#     show_menue ()
#     user_choice = input (" Please enter what do you want to do : ")

#     if user_choice == "1" :
#         english_to_persian ()
    
#     elif user_choice == "2" :
#         persian_to_english ()
    
#     elif user_choice == "3" :
#         add ()
    
#     elif user_choice == "4" :
#         save_to_file ()
#         exit (0)
    
#     else :
#         print (" Your choice is invalid ")
#         print (" Please try again base on the menue ")

from googletrans import Translator
from gtts import gTTS
import os

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

def text_to_speech(text, lang, filename):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    os.system(f"start {filename}")  # This line is for Windows. Use 'open' for Mac or 'xdg-open' for Linux.

def main():
    print("Select translation direction:")
    print("1: English to Persian")
    print("2: Persian to English")
    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        src_lang = "en"
        dest_lang = "fa"
        tts_lang = "fa"
    elif choice == "2":
        src_lang = "fa"
        dest_lang = "en"
        tts_lang = "en"
    else:
        print("Invalid choice")
        return

    text = input("Enter text to translate: ")
    translated_text = translate_text(text, src_lang, dest_lang)
    print(f"Translated text: {translated_text}")

    filename = "translated_audio.mp3"
    text_to_speech(translated_text, tts_lang, filename)

if __name__ == "__main__":
    main()
