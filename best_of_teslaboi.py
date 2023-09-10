from choice_helper import choice_helper
from magic_text import magic_text
from morse_translator import morse_translator
from writer import writer

i = 5
while i < 10:
    print('''|The Best Of Teslaboi!|
            All of Tesla's cool programs in one!
        ''')
    print('''There are 4 programs to choose from:
            Choice Helper
            Magic Text
            Morse Translator
            Writer
          Or you can write stop to close the program!
        ''')
    program_choice = input('Write the name of the feature you want to use: ').lower()
    
    if  program_choice == 'choice helper':
        choice_helper()
        print('''
        ''')
    elif program_choice == 'magic text':
        magic_text()
        print('''
        ''')
    elif program_choice == 'morse translator':
        morse_translator()
        print('''
        ''')
    elif program_choice == 'writer':
        writer()
        print('''
        ''')
    