from choice_helper import choice_helper
from magic_text import magic_text
from morse_translator import morse_translator
from writer import writer

while True:
    print('''|The Best Of Teslaboi!|
            All of Tesla's cool programs in one!
        ''')
    print('''There are 4 programs to choose from:
            1) Choice Helper
            2) Magic Text
            3) Morse Translator
            4) Writer
        ''')
    program_choice = input('Write the number of the program you want to use in this list: ').lower()
    if program_choice == '1':
        choice_helper()
    elif program_choice == '2':
        magic_text()
    elif program_choice == '3':
        morse_translator()
    elif program_choice == '4':
        writer()