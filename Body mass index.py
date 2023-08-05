print("Welcome to the system")
a = int(input("Please write your weight:"))
b = float(input("Please write your height"))
print("Please wait.... Your body mass index is being calculated.")
c = a / (b**2)
if c < 18.5:
    print("Underweight")
elif c >= 18.5 and 25 > c:
    print("Normal")
elif c >= 25 and 30 > c:
    print("Overweight")
elif c >= 30 and 35 > c:
    print("Obese")
elif c >= 35:
    print("Extremely Obese")
