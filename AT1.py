import math
import sys

def display_menu():
    print("\nWelcome to the Long Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Square Root (√)")
    print("7. Logarithm (log)")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")
    print("11. Quit")

def perform_operation(choice, current_value=None):
    # Read values and compute the chosen operation
    if choice in [1, 2, 3, 4, 5]:  # Binary operations
        if current_value is not None:
            num1 = current_value
        else:
            num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            return num1 + num2
        elif choice == 2:
            return num1 - num2
        elif choice == 3:
            return num1 * num2
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero!")
                return None
            return num1 / num2
        elif choice == 5:
            return num1 ** num2

    elif choice == 6:  # Square Root
        num = current_value if current_value is not None else float(input("Enter the number: "))
        if num < 0:
            print("Error: Square root of a negative number is not defined!")
            return None
        return math.sqrt(num)

    elif choice == 7:  # Logarithm
        num = current_value if current_value is not None else float(input("Enter the number: "))
        if num <= 0:
            print("Error: Logarithm undefined for non-positive numbers!")
            return None
        return math.log(num)

    elif choice in [8, 9, 10]:  # Trigonometric Functions
        num = current_value if current_value is not None else float(input("Enter the angle in degrees: "))
        radians = math.radians(num)  # Convert degrees to radians
        if choice == 8:
            return math.sin(radians)
        elif choice == 9:
            return math.cos(radians)
        elif choice == 10:
            return math.tan(radians)

def long_calculator():
    current_value = None
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-11): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 11.")
            continue

        if choice == 11:
            print("Exiting the calculator. Goodbye!")
            sys.exit()

        if 1 <= choice <= 10:
            try:
                current_value = perform_operation(choice, current_value)
                if current_value is not None:
                    print(f"Result: {current_value}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid choice. Please try again.")

# Run the long calculator
if __name__ == "__main__":
    long_calculator()
