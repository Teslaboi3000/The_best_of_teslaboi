def morse_translator():  
    alphabet_to_morse = {
        'a': '._ ', 'b': '_... ', 'c': '_._. ', 'd': '_.. ', 'e': '. ',
        'f': '.._. ', 'g': '__. ', 'h': '.... ', 'i': '.. ', 'j': '.___ ',
        'k': '_._ ', 'l': '._.. ', 'm': '__ ', 'n': '_. ', 'o': '___ ',
        'p': '.__. ', 'q': '__._ ', 'r': '._. ', 's': '... ', 't': '_ ',
        'u': '.._ ', 'v': '..._ ', 'w': '.__ ', 'x': '_.._ ', 'y': '_.__ ',
        'z': '__.. ', ' ': ' / ', '0': '_____ ', '1': '.____ ', '2': '..___ ',
        '3': '..._ ', '4': '...._ ', '5': '..... ', '6': '_.... ', '7': '__... ',
        '8': '___.. ', '9': '____. ', ',': '__..__ ', ':': '___... ', '?': '..__.. ',
        '=': '_..._ ', '(': '_.__. ', ')': '_.__._ ', '"': '._.._. ', "'": '.____. ',
        '/': '_.._. ', '@': '.__._. ', '!': '_._.__ '
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
