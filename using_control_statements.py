is_stop = False

while is_stop == False:

    try:
        user_input = input("Input Age: ")
        age = int(user_input)
        description = ""

        if age > 18:
            description = "an adult"
        elif age >= 14:
            description = "in high school"
        elif age > 10:
            description = "in middle school"
        elif age > 3:
            description = "in preschool"
        elif age >= 0:
            description = "an infant"
        elif age < 0:
            description = "that is impossible"
        else:
            description = "in grade school"

        print(f"""The person is {age} years old and {description}.""")

    except ValueError:
        if type(user_input) == "str":
            is_stop = True
            continue

    except KeyboardInterrupt:
        print("Program is exiting...");
        is_stop = True