#!/usr/bin/env python3.6

over_weight = float(25)
skinny_weight = float(18)

def gather_info():
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (pounds or kilograms) "))
    system = input("Are your mearsurements in metric or imperial systems? ").lower().strip()
    return (height, weight, system)


def calculate_bmi(weight, height, system='metric'):
    if system == 'metric':
       bmi = (weight / (height ** 2))
    else:
       bmi = 703 * (weight / (height ** 2))
    return bmi


while True:
     height, weight, system = gather_info()
     if system.startswith('i'):
        bmi = calculate_bmi(weight, system='imperial', height=height)
        print(f"Your BMI is {bmi}")
        if bmi >= over_weight:
            print(f"You are fat")
        elif bmi <= skinny_weight:
            print(f"You are skinny")
        else:
            print(f"You are normal")
        break
     elif system.startswith('m'):
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi}")
        if bmi >= over_weight:
            print(f"You are fat")
        elif bmi <= skinny_weight:
            print(f"You are skinny")
        else:
            print(f"You are normal")
        break
     else:
        print("Error: Unknown measurement system. Please use imperial or metric.")