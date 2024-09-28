import math

def circle():
    radius = float(input("Enter the radius of the circle in centimetre: "))
    circle_circumference = 2 * math.pi * radius
    circle_area = math.pi * pow(radius, 2)
    print(f"The circumference of the circle is {round(circle_circumference, 2)} cm")
    print(f"The area of the circle is {round(circle_area, 2)} cm^2\n\n")

def hypotenuse():
    print("Type measurement in centimetres!!")
    side_a = float(input("Enter side A: "))
    side_b = float(input("Enter side B: "))
    hypotenuse = round(math.sqrt(pow(side_a, 2) + pow(side_b, 2)), 2)
    print(f"The hypotenuse of the triangle is {hypotenuse} cm\n\n")

def arithmetic():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    operation = input("What do you want to do with ( + , - , * , / , % ): ")

    try:
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else "Undefined",
            '%': lambda a, b: a % b if b != 0 else "Undefined"
        }

        if operation in operations:
            result = operations[operation](x, y)
            if result == "Undefined":
                print("Undefined")
            else:
                print(f"The result is {round(result, 2)}\n\n")
        else:
            print("Please enter a valid operation (+, -, *, /)")
    except ValueError:
        print("Please enter valid numbers")
    except Exception as e:
        print(f"Something went wrong: {e}")

def main_menu():
    last_operation = None
    process = True
    while process:
        try:
            if last_operation:
                next_step = input("Choose an option: \n1. Go back to menu \n2. Calculate again \n3. Stop \nEnter your choice (1, 2, or 3): ")
            else:
                calculate = input("Circle Area|Circumference, Hypotenuse of triangle, Two numbers[C:H:T] ---- ").upper()
                options = {
                    'C': circle,
                    'H': hypotenuse,
                    'T': arithmetic
                }

                if calculate in options:
                    options[calculate]()
                    last_operation = options[calculate]  # Store the last operation
                else:
                    print("This function is not supported for now.")
                continue 

            if next_step == '1':
                last_operation = None  # Reset last operation when going back to the menu
                continue  # Go back to menu
            elif next_step == '2':
                if last_operation:
                    last_operation()  # Call the last operation again
                else:
                    print("No previous operation to repeat.")
            elif next_step == '3':
                process = False
                print("GOOD BYE!")
            else:
                print("Invalid choice, returning to menu.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main_menu()
