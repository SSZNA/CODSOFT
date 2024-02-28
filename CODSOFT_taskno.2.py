def AddNum(Num1,Num2):
    result = Num1 + Num2
    print(f"Sum: {result:.2f}")

def SubtractNum(Num1,Num2):
    if Num1>Num2:
        result = Num1 - Num2
    elif Num2>Num1:
        result = Num2 - Num1
    print(f"Difference: {result:.2f}")

def MultiplyNum(Num1,Num2):
    result = Num1 * Num2
    print(f"Result: {result:.2f}")

def DivideNum(Num1,Num2):
    if Num2 == 0:
        print("Cannot be divided by zero!")
    else:
        result = Num1/Num2
        print(f"Result after division: {result:.2f}")


def main():
    print("     SIMPLE CALCULATOR     ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operations = ["1","2","3","4"]
    option = input("Select an option: ")
    if option in operations:
        Num1 = float(input("Enter first number: "))
        Num2 = float(input("Enter second number: "))
        if option == "1":
            AddNum(Num1,Num2)
        elif option == "2":
            SubtractNum(Num1,Num2)
        elif option == "3":
            MultiplyNum(Num1,Num2)
        elif option == "4":
            DivideNum(Num1,Num2)
    else:
        print("Choice is invalid!")

main()

