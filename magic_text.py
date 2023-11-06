def magic_text():
      import random      
      
      i = 5
      print('''Magic Text, the evolution of the magic ball!
            by Teslaboi_3000| You can start with your questions! Write exit to close''')
      while True:
            user_input = input("> ")
            answers = ["I don't think so", "Use immagination!", "Too simp", "In your dreams maybe!", "Maybe! (if you're a baby)", "Impossible!", "Nuh uh", "Maybe!", "Absolutley yes", "Yuh uh"]
            answer = random.choice(answers)
            print(answer)
            if user_input == 'exit':
                  exit()