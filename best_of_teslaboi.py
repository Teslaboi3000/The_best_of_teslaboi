from choice_helper import choice_helper
from magic_text import magic_text
from morse_translator import morse_translator
from writer import writer


print("|The Best Of Teslaboi!|\nAll of Tesla's cool programs in one!\n")
while True:
    print('''There are 4 programs to choose from:
            1) Choice Helper
            2) Magic Text
            3) Morse Translator
            4) Writer
        ''')
    program_choice = input('Write the number of the program you want to use in this list (or write exit to close the program): ').lower()
    if program_choice == '1':
        choice_helper()
    elif program_choice == '2':
        magic_text_language = input("In what language do you want to use Magic Text? 1)English > ")
        if magic_text_language == "1":
            magic_text()
        else:
            print("Uhm, still gotta learn that language.")
    elif program_choice == '3':
        morse_translator()
    elif program_choice == '4':
        writer()
    elif program_choice == 'exit':
        exit()