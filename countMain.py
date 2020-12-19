

def frequencyDigits(n, d):
    # Counter variable to
    # store the frequency
    c = 0;
    # iterate till number
    # reduces to zero
    while (n > 0):

        # check for equality
        if (n % 10 == d):
            c += 1;
            # reduce the number
        n = int(n / 10);
    if (c != 0):
        print(d, ' appears ', c, ' times')

def inputHandling(inputValue):
    if (inputValue == 'Quit'):
        finished == 2
    elif(inputValue.isdigit()):
        inputValue = int(inputValue)
        i = 0
        while (i < 9):
            frequencyDigits(inputValue, i)
            i = i + 1
    else:
        print('You have entered an invalid input. Please try again')

finished = 1
while(finished==1):
    inputValue = input("Please enter a number or type 'Quit' to exit the program")
    inputHandling(inputValue)
