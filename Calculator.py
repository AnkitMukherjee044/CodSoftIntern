def add(x,y):
    return x + y

def Subtract(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    if y != 0:
        return x/y
    else:
        print("Error:y value is 0")

def main():
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter your choice (1-5):")

        if choice in('1','2','3','4'):
            num1 = float(input("Enter the first number:"))
            num2 = float(input("Enter te second number:"))

            if choice == '1':
                print(f"Result: {add(num1,num2)}")
            elif choice == '2':
                print(f"Result: {Subtract(num1,num2)}")
            elif choice == '3':
                print(f"Result: {multiplication(num1,num2)}")
            elif choice == '4':
                print(f"Result: {division(num1,num2)}")
            elif choice == '5':
                print("Goodbye!")
            else:
                print("Invalid choice,please enter a number between 1 - 5.")


if __name__ == "__main__":
    main()
    