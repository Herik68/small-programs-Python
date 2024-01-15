principle = 0
rate =0
time =0

try:
    while principle <= 0:
        principle = float(input("Enter the principle amount:"))
        if principle <= 0:
            print("Principle can't be less than or equal to zero.")
    while rate <= 0:
        rate = float(input("Enter the interest rate in percent:"))
        if rate <= 0:
            print("Rate can't be less than or equal to zero.")
    while time <= 0:
        time = float(input("Enter the time in years:"))
        if time <= 0:
            print("Time can't be less than or equal to zero.")
    total = principle * pow((1 + rate / 100), time)

    print(f"Balance after {time} years : ${total:.2f}")
except ValueError:
    print("Please enter numbers only!!!")

