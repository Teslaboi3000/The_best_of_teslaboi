def writer():
    print('''Welcome to Writer! A useless but cool program!
        ''')
    message = input("What do you want to write? ")
    number_of_times = int(input("How many times do you want to write it? "))

    visible_percentage = int(input("Do you want the percentage to be visible? Press 1 if you want it to be visible, 0 if you don't. "))

    if visible_percentage == 1:
        for i in range(number_of_times + 1):
            print(f"{message} {i}%")
    elif visible_percentage == 0:
        for i in range(number_of_times):
            print(f"{message}")
