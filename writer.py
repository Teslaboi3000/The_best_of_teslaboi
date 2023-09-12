def writer():
    print("Welcome to Writer! A simple but useful program!\n")

    message = input("What do you want to write? ")
    number_of_times = int(input("How many times do you want to write it? "))

    visible_percentage = int(input("Do you want the percentage to be visible? Press 1 if you want it to be visible, 0 if you don't. "))

    if visible_percentage == 1:
        for i in range(number_of_times + 1):
            output = (i / number_of_times) * 100
            print(f"{message} {int(output)}%")
    elif visible_percentage == 0:
        for i in range(number_of_times):
            print(message)
