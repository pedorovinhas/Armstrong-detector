def Armstrong_Calculator(OriginalNumber):
    while True:
        count = 0
        number = OriginalNumber

        while (number > 0):
            number = number//10
            count = count + 1

        #list of digits in the typed number
        digits = [int(x) for x in str(OriginalNumber)]
        #raising all digits to the power of the count of digits
        multiplied = [i ** count for i in digits]
        #summing the raised numbers
        totalsum = sum(multiplied)
        
        if totalsum == OriginalNumber:
            print(f"{OriginalNumber} is an Armstrong number.")
        else:
            print(f"{OriginalNumber} is not an Armstrong number.")

yes = ["Yes", "yes", "y", "Initiate", "Begin", "initiate", "begin"]
no = ["No", "no", "n", "quit", "Quit", "Fuck you"]

while True:    
    begin = input("Initiate Armstrong Number Calculator?")
    if begin in yes:
        OriginalNumber = input("Type a number to be calculated, or two numbers(separated by commas)")
        Armstrong_Calculator(OriginalNumber)
    elif begin in no:
        break
    else:
        print("Please type an adequate answer.")
