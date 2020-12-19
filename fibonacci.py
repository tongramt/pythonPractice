# First eTest
# Create a for loop that prints the numbers in a fibonacci sequence up to a specified limit

finished = 0
while finished == 0:
    try:
        inputValue = int(input("Please input a number and the program will output"
                         " the two previous numbers in the Fibonacci sequence: "))
    except ValueError:
            print("Please rerun the code and enter a number")

    firstFib = int(1)
    secondFib = int(2)
    if inputValue.isdigit():
        fibLimit = int(inputValue)
        if fibLimit <= 0:

            print("The input wich you have entered does not allow the program"
                  " does \nnot allow it to compute the two lower numbers in the Fibonacci sequence.\n"
                  "Please try again.")

        elif fibLimit == 1:

            print('You have entered 1 as the limit. 1 Is itself in the Fibonacci sequence but there'
                  ' \nare no numbers before it.')
            finished = 1

        elif fibLimit == 2:

            print('You have entered 2 as the limit. 2 Is itself in the Fibonacci sequence but there'
                ' \nais only one number before it the number 1.')
            finished = 1

        while finished == 0:

            thirdFib = firstFib + secondFib
            if thirdFib == fibLimit:
                print("%d is already in the Fibonacci sequence. The previous two numbers\n"
                          "are %d and %d." % (thirdFib, firstFib, secondFib))
                finished = 1

            elif thirdFib > fibLimit:
                print("The limit you have entered is %d. The previous two numbers in the Fibonaci sequence are\n"
                          "are %d and %d." % (fibLimit, firstFib, secondFib))
                finished = 1
            else:
                firstFib = secondFib
                secondFib = thirdFib

    else:
        print('The input you have entered is invalid please try again')







