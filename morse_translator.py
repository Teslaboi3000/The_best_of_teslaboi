def morse_translator():  
    alphabet_to_morse = {
        'a': '._ ', 'b': '_... ', 'c': '_._. ', 'd': '_.. ', 'e': '. ',
        'f': '.._. ', 'g': '__. ', 'h': '.... ', 'i': '.. ', 'j': '.___ ',
        'k': '_._ ', 'l': '._.. ', 'm': '__ ', 'n': '_. ', 'o': '___ ',
        'p': '.__. ', 'q': '__._ ', 'r': '._. ', 's': '... ', 't': '_ ',
        'u': '.._ ', 'v': '..._ ', 'w': '.__ ', 'x': '_.._ ', 'y': '_.__ ',
        'z': '__.. ', ' ': ' / ', '0': '----- ', '1': '.---- ', '2': '..--- ',
        '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ',
        '8': '---.. ', '9': '----. ', ',': '--..-- ', ':': '---... ', '?': '..--.. ',
        '=': '-...- ', '(': '-.--. ', ')': '-.--.- ', '"': '._.._. ', "'": '.----. ',
        '/': '-.._. ', '@': '.--.-. ', '!': '-.-.-- '
    }

    morse_to_alphabet = {value.strip(): key for key, value in alphabet_to_morse.items()}

    print('''Welcome to Teslaboi's and Maxjustuniversal's Morse code translator!
          ''')
    writing_reading = input('Write or read Morse: ')

    if writing_reading == 'write':
        message = input('Write message: ').lower()
        output = ''
        for character in message:
            if character in alphabet_to_morse:
                output += alphabet_to_morse[character]
            else:
                output += ' '  
        print(output)

    elif writing_reading == 'read':
        message = input('Read message: ')
        morse_words = message.split(' / ')
        output = ''
        for morse_word in morse_words:
            morse_characters = morse_word.split()
            for morse_character in morse_characters:
                if morse_character in morse_to_alphabet:
                    output += morse_to_alphabet[morse_character]
                else:
                    output += '?'  
            output += ' '  
        print(output.strip())  
