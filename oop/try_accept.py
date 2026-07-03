print("Safe Division er jonno try-except block use kora hoyeche.")

while True:
    try:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        result = num1 / num2 
        print(f"Result:{result}")
        break
    except ValueError:
        print()