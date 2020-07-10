def armstrong_calculator(x):
    while True:
        count = 0
        number = int(x)

        while number > 0:
            number = number // 10
            count = count + 1

        # list of digits in the typed number
        digits = [int(a) for a in str(x)]
        # raising all digits to the power of the count of digits
        multiplied = [i ** count for i in digits]
        # summing the raised numbers
        totalsum = sum(multiplied)

        if totalsum == x:
            usefunc()
            return True
        else:
            usefunc()
            return False


# def inputTrue()
#    inputNumber = input("Type a number to be calculated, or two numbers(separated by commas)")
#    if inputNumber.isnumeric():
#        Armstrong_Calculator(inputNumber)

yes = ["Yes", "yes", "y", "Initiate", "Begin", "initiate", "begin"]

no = ["No", "no", "n", "quit", "Quit", "Fuck you"]
use = 0


def usefunc():
    global use
    use += 1


while use < 1:
    begin = input("Initiate Armstrong Number Calculator?")
    if begin in yes:
        inputNumber = input("Type a number to be calculated, or two numbers(separated by commas)").lower()
        if inputNumber.isnumeric():
            if armstrong_calculator(inputNumber) == True:
                print(f"{inputNumber} is an armstrong number.")
            else:
                print(f"{inputNumber} is not an armstrong number.")
        elif inputNumber[0:4] == "from":
            lista = inputNumber.split()
            lista.remove("from")
            lista.remove("to")
            lista = list(map(int, lista))
            for i in range(lista[0], lista[1]):
                resultados = []
                armstrong_calculator(i)
                if armstrong_calculator(i) == True:
                    resultados.append(i)
                i =+ 1
            print(resultados)

    elif begin in no:
        break
    else:
        print("Please type an adequate answer.")
