print("BMI Calculator")

try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
except ValueError:
    print("Please enter valid numerical values for weight and height.")
    quit()

if weight <= 0 or height <= 0:
    print("Please enter valid positive values for weight and height.")
    quit()

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")
