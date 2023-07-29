while True:
    answer = input("Take the color quiz: ").lower()

    if answer == "yes":
        color = input("What is your favorite color?:")
        print("Your Favorite Color is " +color)
        break

    elif answer == "no":
        print(">:) die")
        break  # End the loop when the user enters "no"

    else:
        print("Pick 'yes' or 'no' >:)")
