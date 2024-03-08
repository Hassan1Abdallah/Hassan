# Hassan Abdallah Hassan Mohamed     20230123
# Mariam Muhammad Youssef Sharnoubi  20230398
# Menna Samir Mohamed Elmetenawy     20220346


"""
comment test cases
decimal to binary        23 --> 10111
decimal to octal         23 --> 27
decimal to Hexadecimal   23 --> 17

binary to decimal      10110 --> 22
binary to octal        10110 --> 26
binary to Hexadecimal  10110 --> 16

octal to decimal       25 --> 21
octal to binary        25 --> 10101
octal to hexadecimal   25 --> 15

hexadecimal to decimal AB --> 171
hexadecimal to binary  AB --> 10101011
hexadecimal to octal   AB --> 253

"""


# Menu 1 -> display Menu 1
def Menu1():
    print()
    print("Numbering system Converter: ")
    print("(A) Insert a new number")
    print("(B) Exit Program")


# Menu 2 -> display Menu 2
def Menu2():
    print()
    print("(A) Decimal")
    print("(B) Binary")
    print("(C) Octal")
    print("(D) Hexadecimal")


# Menu 3 -> display Menu 3
def Menu3():
    print()
    print("(A) Decimal")
    print("(B) Binary")
    print("(C) Octal")
    print("(D) Hexadecimal")


# Function check the number is decimal
def check_if_decimal(decimal_number):
    while True:
        try:
            decimal_number = int(decimal_number)
            break
        except:
            decimal_number = input("Please enter a valid decimal number: ")
    return decimal_number


# Function from Decimal to Binary:
def decimal_to_binary(decimal_number):
    decimal_number = int(decimal_number)
    binary_num = ""
    while decimal_number > 0:
        remainder = decimal_number % 2  # Calculate the remainder when dividing by 2
        binary_num = str(remainder) + binary_num
        decimal_number = decimal_number // 2  # remainder of the division is an integer and not float
    return binary_num


# Function convert from decimal to octal :
def decimal_to_octal(decimal_number):
    decimal_number = int(decimal_number)
    octal_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 8
        octal_number = str(remainder) + octal_number
        decimal_number = decimal_number // 8
    return octal_number


# Function convert from decimal to Hexadecimal :
def decimal_to_hexadecimal(decimal_number):
    decimal_number = int(decimal_number)
    hexadecimal_num = ""
    Hexa_chars = ["A", "B", "C", "D", "E", "F"]  # list of hexadecimal numbers greater then 9
    while decimal_number > 0:
        remainder = decimal_number % 16  # Calculate the remainder when dividing by 2
        if remainder > 9:
            hexadecimal_num = Hexa_chars[remainder - 10] + hexadecimal_num  # use of char from the list (Hexa_decimal)
        else:
            hexadecimal_num += str(remainder)
        decimal_number = decimal_number // 16  # remainder of the division is an integer and not float
    return hexadecimal_num


# Function check if number is Binary:
def check_if_binary(binary_number):
    is_binary = False
    while not binary_number:
        binary_number = input("Please enter a valid binary number: ")
    while not is_binary:
        for digit in binary_number:
            if digit != "0" and digit != "1":
                is_binary = False
                binary_number = input("Please enter a valid binary number: ")
                break
            else:
                is_binary = True
    return binary_number


# Function convert from Binary to Decimal :
def binary_to_decimal(
        binary_number):  # This function converts the binary number entered by the user to a decimal  number
    binary_number = check_if_binary(binary_number)
    decimal = 0
    binary_number = binary_number
    for index in range(len(binary_number)):
        decimal += int(binary_number[-index - 1])(2 * index)
    return decimal


# Function convert from Binary to Octal :
def binary_to_octal(binary_number):  # This function converts the binary number entered by the user to an octal number
    binary_number = check_if_binary(binary_number)
    """
    The number has to be divisible by 3 to divide it into groups of 3 digits. If the number of digits 
    in the binary number is not divisible by three, I'll add zeros on the left(which won't change 
    the value of the number).
    """
    octal = ""
    remainder = len(binary_number) % 3
    if remainder == 1:
        binary_number = "00" + binary_number
    elif remainder == 2:
        binary_number = "0" + binary_number
    """
    To convert a number from binary to octal, we take every 3 binary digits and replace them with the 
    equivalent octal digit.
    """
    initial = 0
    for initial in range(int(len(binary_number) / 3)):
        if binary_number[initial:initial + 3] == "000":
            octal += "0"
        elif binary_number[initial:initial + 3] == "001":
            octal += "1"
        elif binary_number[initial:initial + 3] == "010":
            octal += "2"
        elif binary_number[initial:initial + 3] == "011":
            octal += "3"
        elif binary_number[initial:initial + 3] == "100":
            octal += "4"
        elif binary_number[initial:initial + 3] == "101":
            octal += "5"
        elif binary_number[initial:initial + 3] == "110":
            octal += "6"
        else:
            octal += "7"
        initial += 3
    return octal


# Function convert from Binary to Hexadecimal:
def binary_to_hexadecimal(
        binary_number):  # This function converts the binary number entered by the user to a hexadecimal number
    binary_number = check_if_binary(binary_number)
    """
    The number has to be divisible by 4 to divide it into groups of 4 digits. If the number of digits 
    in the binary number is not divisible by 4, I'll add zeros on the left(which won't change 
    the value of the number). 
    """
    hexadecimal = ""
    remainder = len(binary_number) % 4
    if remainder == 1:
        binary_number = "000" + binary_number
    elif remainder == 2:
        binary_number = "00" + binary_number
    elif remainder == 3:
        binary_number = "0" + binary_number
    """
    To convert a number from binary to hexadecimal, we take every 4 binary digits and replace them with the 
    equivalent hexadecimal digit.
    """
    initial = 0
    for _ in range(int(len(binary_number) / 4)):
        if binary_number[initial:initial + 4] == "0000":
            hexadecimal += "0"
        elif binary_number[initial:initial + 4] == "0001":
            hexadecimal += "1"
        elif binary_number[initial:initial + 4] == "0010":
            hexadecimal += "2"
        elif binary_number[initial:initial + 4] == "0011":
            hexadecimal += "3"
        elif binary_number[initial:initial + 4] == "0100":
            hexadecimal += "4"
        elif binary_number[initial:initial + 4] == "0101":
            hexadecimal += "5"
        elif binary_number[initial:initial + 4] == "0110":
            hexadecimal += "6"
        elif binary_number[initial:initial + 4] == "0111":
            hexadecimal += "7"
        elif binary_number[initial:initial + 4] == "1000":
            hexadecimal += "8"
        elif binary_number[initial:initial + 4] == "1001":
            hexadecimal += "9"
        elif binary_number[initial:initial + 4] == "1010":
            hexadecimal += "A"
        elif binary_number[initial:initial + 4] == "1011":
            hexadecimal += "B"
        elif binary_number[initial:initial + 4] == "1100":
            hexadecimal += "C"
        elif binary_number[initial:initial + 4] == "1101":
            hexadecimal += "D"
        elif binary_number[initial:initial + 4] == "1110":
            hexadecimal += "E"
        else:
            hexadecimal += "F"
        initial += 4
    return hexadecimal


# Function check if number is Octal:
def check_if_octal(octal):
    is_octal = False
    while not octal:
        octal = input("Please enter a valid octal number: ")
    while not is_octal:
        for digit in octal:
            if digit != "0" and digit != "1" and digit != "2" and digit != "3" and digit != "4" \
                    and digit != "5" and digit != "6" and digit != "7":
                is_octal = False
                octal = input("Please enter a valid octal number: ")
                break
            else:
                is_octal = True
    return octal


# Function convert from octal to decimal :
def octal_to_decimal(octal_num):
    octal_num = int(octal_num)
    decimal_num = 0
    i = 0
    while octal_num > 0:
        dijit = octal_num % 10  # The first digit after the decimal point
        decimal_num = decimal_num + dijit * (8 ** i)
        octal_num = octal_num // 10  # // ===>> remainder of the division is an integer and not float
        i += 1
    return decimal_num


# Function convert from octal to Binary:
def octal_to_binary(octal_num):
    octal_num = int(octal_num)
    decimal_num = 0
    i = 0
    while octal_num > 0:
        dijit = octal_num % 10  # The first digit after the decimal point
        decimal_num = decimal_num + dijit * (8 ** i)
        octal_num = octal_num // 10  # // ===>> remainder of the division is an integer and not float
        i += 1
    octal_num = decimal_num
    binary_num = ""
    while octal_num > 0:
        remainder = octal_num % 2  # Calculate the remainder when dividing by 2
        binary_num = str(remainder) + binary_num
        octal_num = octal_num // 2  # remainder of the division is an integer and not float
    return binary_num


# Function convert from octal to Hexadecimal :
def octal_to_hexadecimal(octal):
    binary = octal_to_binary(octal)
    return binary_to_hexadecimal(binary)


# Function check if number is Hexadecimal:
def check_if_hexadecimal(number):
    is_hexadecimal = False
    while not number:
        number = input("Please enter a valid hexadecimal number: ")
    while not is_hexadecimal:
        for digit in number:
            if digit != "A" and digit != "B" and digit != "C" and digit != "D" and digit != "E" and \
                    digit != "F" and digit != "1" and digit != "2" and digit != "3" and digit != "4" \
                    and digit != "5" and digit != "6" and digit != "7" and digit != "8" and digit != "9" \
                    and digit != "0":
                is_hexadecimal = False
                number = input("Please enter a valid hexadecimal number: ")
                break
            else:
                is_hexadecimal = True
    return number


# Function Converting Hexadecimal letters to Decimal numbers:
def Hexa_letters_to_Dec(letter):
    if letter == "A":
        letter = int(10)
    elif letter == "B":
        letter = int(11)
    elif letter == "C":
        letter = int(12)
    elif letter == "D":
        letter = int(13)
    elif letter == "E":
        letter = int(14)
    elif letter == "F":
        letter = int(15)
    return letter


# Function converting from Hexadecimal to Decimal:
def Hexa_to_Dec(Number):
    pow = 0
    final_res = 0
    for digit in Number[::-1]:
        digit = Hexa_letters_to_Dec(digit)
        digit = int(digit)
        final_res += digit * (16 ** pow)
        pow += 1
    return final_res


# Function Converting from Hexadecimal to Binary:
def Hexa_to_Bin(Number):
    final_res = ""
    for digit in Number[::-1]:
        digit = Hexa_letters_to_Dec(digit)  # Convert letters in Hexadecimals to Decimal
        digit = int(digit)
        bin_res = ""
        while digit != 0:  # Convert from decimal to binary
            if digit % 2 == 0:
                bin_res += "0"
            elif digit % 2 != 0:
                bin_res += "1"
            digit = digit // 2
        while len(bin_res) <= 3:
            bin_res += "0"
        final_res += bin_res
    final_res = final_res[::-1]  # Reverse the final result
    return final_res


# Function Convert from Hexadecimal to Octal
def Hexa_to_Octal(Number):
    Number = Hexa_to_Bin(Number)  # Converting from Hexadecimal to Binary
    Number = binary_to_octal(Number)  # Converting from Binary to Octal
    if Number[0] == "0":  # Remove the Zeros From the Left
        Number = Number[1::]
    return Number


choice1 = None  # variable for selecting from the Menu 1

while choice1 != "B":
    Menu1()  # calling function Menu 1
    choice1 = input("Select an option from the Menu : ").upper()

    # If user entered a wrong choice:
    while choice1 != "A" and choice1 != "B":  # True
        Menu1()  # Display Menu
        choice1 = input("Please select a valid choice : ").upper()  # Error Message

    if choice1 != "B":  # If User choose A
        Number = input("Please insert a number: ").upper()
        Menu2()
        choice2 = input("Select the base you want to convert a number from: ").upper()

        # If user entered a wrong choice:
        while choice2 != "A" and choice2 != "B" and choice2 != "C" and choice2 != "D":  # True
            Menu2()  # Display Menu
            choice2 = input("Please select a valid choice : ").upper()  # Error Message

        if choice2 == "A":  # Base Decimal
            Number = str(check_if_decimal(Number))
            Menu3()
            choice3 = input("Please select the base you want to convert a number to : ").upper()

            # If user entered a wrong choice:
            while choice3 != "A" and choice3 != "B" and choice3 != "C" and choice3 != "D":  # True
                Menu3()  # Display Menu
                choice3 = input("Please select a valid choice : ").upper()  # Error Message

            if choice3 == "A":  # From Decimal to Decimal
                print(f"The Number in Decimal : {Number}")  # Display the same input

            elif choice3 == "B":  # From Decimal to Binary
                Number = decimal_to_binary(Number)
                print(f"The Number in Binary : {Number}")

            elif choice3 == "C":  # From Decimal to Octal
                Number = decimal_to_octal(Number)
                print(f"The Number in Octal : {Number}")

            elif choice3 == "D":  # From Decimal to Hexadecimal
                Number = decimal_to_hexadecimal(Number)
                print(f"The Number in Hexadecimal : {Number}")

        elif choice2 == "B":  # Base Binary
            # Convert from binary
            # Show Menu 3 and get user's choice
            Menu3()
            choice3 = input("Please select the base you want to convert a number to : ").upper()
            # If user entered a wrong choice:
            while choice3 != "A" and choice3 != "B" and choice3 != "C" and choice3 != "D":  # True
                Menu3()  # Display Menu
                choice3 = input("Please select a valid choice : ").upper()  # Error Message

            if choice3 == "A":  # Binary to Decimal
                Number = binary_to_decimal(Number)
                print(f"The Number in Decimal : {Number}")

            elif choice3 == "B":  # From Binary to Binary
                Number = check_if_binary(Number)
                print(f"The Number in Binary : {Number}")  # Display the same input

            elif choice3 == "C":  # From Binary to Octal
                Number = binary_to_octal(Number)
                print(f"The Number in Octal : {Number}")

            elif choice3 == "D":  # From Binary to Hexadecimal
                Number = binary_to_hexadecimal(Number)
                print(f"The Number in Hexadecimal : {Number}")

        elif choice2 == "C":  # Base Octal
            # Convert from octal
            # Show Menu 3 and get user's choice
            Number = str(check_if_octal(Number))
            Menu3()
            choice3 = input("Please select the base you want to convert a number to : ").upper()

            # If user entered a wrong choice:
            while choice3 != "A" and choice3 != "B" and choice3 != "C" and choice3 != "D":  # True
                Menu3()  # Display Menu
                choice3 = input("Please select a valid choice : ").upper()  # Error Message

            if choice3 == "A":  # From Octal to Decimal
                Number = octal_to_decimal(Number)
                print(f"The Number in Decimal : {Number}")

            elif choice3 == "B":  # From Octal to Binary
                Number = octal_to_binary(Number)
                print(f"The Number in Binary : {Number}")

            elif choice3 == "C":  # From Octal to Octal
                print(f"The Number in Octal : {Number}")  # Display the same input

            elif choice3 == "D":  # From octal to Hexadecimal
                Number = octal_to_hexadecimal(Number)
                print(f"The number in hexadecimal: {Number}")

        elif choice2 == "D":  # Base Hexadecimal
            # Convert from hexadecimal
            # Show Menu 3 and get user's choice
            Number = check_if_hexadecimal(Number)
            Menu3()
            choice3 = input("Please select the base you want to convert a number to : ").upper()

            # If user entered a wrong choice:
            while choice3 != "A" and choice3 != "B" and choice3 != "C" and choice3 != "D":  # True
                Menu3()  # Display Menu
                choice3 = input("Please select a valid choice : ").upper()  # Error Message

            if choice3 == "A":  # From HexaDecimal to Decimal
                Number = Hexa_to_Dec(Number)
                print(f"The Number in Decimal : {Number}")

            elif choice3 == "B":  # From HexaDecimal to Binary
                Number = Hexa_to_Bin(Number)
                print(f"The Number in Binary : {Number}")

            elif choice3 == "C":  # From HexaDecimal to Octal
                Number = Hexa_to_Octal(Number)
                print(f"The Number in Octal : {Number}")

            elif choice3 == "D":  # From HexaDecimal to Hexadecimal
                print(f"The Number in Hexadecimal : {Number}")  # Display the same input

        else:
            print("Please select a valid choice")