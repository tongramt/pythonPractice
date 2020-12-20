def findSmall(num1, num2, num3):
    if num1<num2 and num1<num3:
        print(num1)
    elif num2<num1 and num2<num3:
        print(num2)
    elif num3<num1 and num3<num2:
        print(num3)

finished=1
while (finished == 1):
    input1, input2, input3 = input("Please enter 3 integers (separated by a comma) and we will return the smallest or type 'Quit': ").split(",")
    # if (input1.isdigit() and input2.isdigit() and input3.isdigit()):
    if (input1.isdigit() and input2.isdigit() and input3.isdigit()):
        input1 = int(input1)
        input2 = int(input2)
        input3 = int(input3)
        findSmall(input1, input2, input3)

    elif (input1 == 'Quit'):
        print('Thanks for using the code')
        finished == 2


    # else:
    #     print('One or more of the inputs you entered is invalid please try again.')