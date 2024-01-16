import math


def circle():
    radius = float(input("Enter the radius of the circle in centimetre:"))
    circle_circumference = 2 * math.pi * radius
    circle_area = math.pi * pow(radius, 2)
    print(f"The circumference of the circle is {round(circle_circumference, 2)} cm")
    print(f"The area of the circle is {round(circle_area, 2)} cm^2")


def hypotenuse():
    print("Type measurement in centimetres!!")
    side_a = float(input("Enter side A:"))
    side_b = float(input("Enter side B:"))
    hypotenuse = round(math.sqrt(pow(side_a, 2) + pow(side_b, 2)), 2)
    print(f"The hypotenuse of the triangle is {hypotenuse} cm")


def arithmetic():
    x = float(input("Enter first number:"))
    y = float(input("Enter second number:"))
    operation = input("What do you want to do with (+, -, *, /):")

    try:
        if operation == "+":
            result = x + y
            print(f"The sum of the numbers is {round(result, 2)}")
        elif operation == "-":
            result = x - y
            print(f"The difference between the numbers is {round(result, 2)}")
        elif operation == "*":
            result = x * y
            print(f"The product of the numbers is {round(result, 2)}")
        elif operation == "/":
            if y != 0:
                result = x / y
                print(f"The division of the numbers is {round(result, 2)}")
            else:
                print("Undefined")
        else:
            print("Please enter a valid operation (+, -, *, /)")
    except ValueError:
        print("Please enter valid numbers")
    except Exception as e:
        print(f"Something went wrong: {e}")


process = True
while process:
    try:
        calculate = input("Circle Area|Circumference, Hypotenuse of triangle, Two numbers[C:H:T]----").upper()

        if calculate == "C":
            circle()
        elif calculate == "H":
            hypotenuse()
        elif calculate == "T":
            arithmetic()
        else:
            print("I'm sorry! This function is not supported for now.")
    except Exception as e:
        print(f"Error: {e}")

    if not input("Press R to calculate again/Press any other key to exit:").upper() == "R":
        process = False
        print("GOOD BYE!")
