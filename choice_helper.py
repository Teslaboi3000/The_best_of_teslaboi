def choice_helper():
      import random
      print('''Choice Helper!
            When you just can't make a choice, there is this program!
            Give me 5 options and ill choose the best one!
            ''')
      
      number_of_choices = input("How many choices you got? (minimum is 2, max is 5) > ")

      if number_of_choices == "2":
            choice1 = input("1st Choice: ")
            choice2 = input("2nd Choice: ")
            choices = [choice1, choice2]
            decision = random.choice(choices)
            print(f'''Mhhhh...You should choose {decision}
            ''')
            
      elif number_of_choices == "3":
            choice1 = input("1st Choice: ")
            choice2 = input("2nd Choice: ")
            choice3 = input("3rd Choice: ") 
            choices = [choice1, choice2, choice3]
            decision = random.choice(choices)
            print(f'''Mhhhh...You should choose {decision}
            ''')
            
      elif number_of_choices == "4":
            choice1 = input("1st Choice: ")
            choice2 = input("2nd Choice: ")
            choice3 = input("3rd Choice: ")
            choice4 = input("4th Choice: ")
            choices = [choice1, choice2, choice3, choice4]
            decision = random.choice(choices)
            print(f'''Mhhhh...You should choose {decision}
            ''')

      elif number_of_choices == "5":
            choice1 = input("1st Choice: ")
            choice2 = input("2nd Choice: ")
            choice3 = input("3rd Choice: ")
            choice4 = input("4th Choice: ")
            choice5 = input("5th Choice: ")
            choices = [choice1, choice2, choice3, choice4, choice5]
            decision = random.choice(choices)
            print(f'''Mhhhh...You should choose {decision}
            ''')
            
