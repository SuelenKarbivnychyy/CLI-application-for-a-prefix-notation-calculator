"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
#pseudocode
#create a function
#ask user to imput the operation and numbers
#tokenize the imput from user
#make the program room forever until be quite for the user


continue_work = True

while continue_work:
    user_question = input("Please type what operation would your like to do, choose an operation from: add, subtract, multiply, divide, square, cube, power, mod. Followed by the numbers you would like to operate with: ")
    tokenize = user_question.split(" ")
    operator = tokenize[0]
    if operator == "q":
        continue_work = False
    else:
        if operator == "square" or operator == "cube":
            if len(tokenize) == 2:
                index_1 = float(tokenize[1])
                if operator == "square":
                    print(square(index_1))
                if operator == "cube":
                    print(cube(index_1))           
            else:
                print("This operator takes only 1 number.")
