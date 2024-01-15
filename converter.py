#Python weight converter

weight= float(input("Enter your weight:"))
unit  = input("Killogram(K) or Pound(L)?")
if  unit == "K":
    weight=weight*2.205
    unit = "lbs"
    print(f"Your weight is {round(weight,1)} {unit}.")
elif unit == "L":
    weight=weight /2.205
    unit= "kgs"
    print(f"Your weight is {round(weight, 1)} {unit}.")
else:
    print(f"{unit} is not a valid unit!")