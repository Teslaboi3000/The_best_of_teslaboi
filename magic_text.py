def magic_text():
      import random      
      
      i = 5
      print('''Magic Text, the evolution of the magic ball!
            by Teslaboi_3000| You can start with your questions! Write stop to close''')
      while i < 10:
            user_input = input("> ")
            answers = ["Impossible!", "Nuh uh", "Maybe!", "Absolutley yes", "Yuh uh"]
            answer = random.choice(answers)
            print(answer)
            if user_input == 'stop':
                  i += 10