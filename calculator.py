def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "cannot divide by zero"
    return a/b

while True:
    print("\n🧮 Welcome to the Simple Calculator")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice= input("Enter your choice(1-5): ")

    if choice=="5":
        print("🙏 Thanks for using the calculator. 👋 See you next time!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))

    elif choice == '2':
        print("Result:", subtract(num1, num2))

    elif choice == '3':
        print("Result:", multiply(num1, num2))

    elif choice == '4':
        print("Result:", divide(num1, num2))

    else:
        print("⚠️ Invalid input. Please enter a number from 1 to 5.")
      