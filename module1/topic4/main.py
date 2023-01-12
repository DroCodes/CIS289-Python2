"""
   Name: Deon Daigh
   Date: 01/12/2023
   Module 1 Topic 4 Assignment
"""

valid_age = False
valid_coverage_level = False

name = input("Please enter the drivers name")

while not valid_age:
    try:
        age = int(input("Please enter the drivers age"))
    except ValueError:
        print("You must enter an integer")
    else:
        valid_age = True

while not valid_coverage_level:
    coverage_level = input("Please enter the coverage level desired (SM, L, F)")

    if coverage_level.lower() == "sm" or coverage_level == "l" or coverage_level == "f":
        valid_coverage_level = True

driver_data = {"1":[name, age, coverage_level], "cost": 0}

if age >= 16 and age < 25 and coverage_level == "sm":
    driver_data["cost"] = 2593
elif age >= 16 and age < 25 and coverage_level == "l":
    driver_data["cost"] = 2957
elif age >= 16 and age < 25 and coverage_level == "f":
    driver_data["cost"] = 3630
elif age >= 25 and age < 35 and coverage_level == "sm":
    driver_data["cost"] = 608
elif age >= 25 and age < 35 and coverage_level == "l":
    driver_data["cost"] = 691
elif age >= 25 and age < 35 and coverage_level == "f":
    driver_data["cost"] = 1745
elif age >= 35 and age < 45 and coverage_level == "sm":
    driver_data["cost"] = 552
elif age >= 35 and age < 45 and coverage_level == "l":
    driver_data["cost"] = 691
elif age >= 35 and age < 45 and coverage_level == "f":
    driver_data["cost"] = 1564
elif age >= 45 and age < 55 and coverage_level == "sm":
    driver_data["cost"] = 525
elif age >= 45 and age < 55 and coverage_level == "l":
    driver_data["cost"] = 596
elif age >= 45 and age < 55 and coverage_level == "f":
    driver_data["cost"] = 1469
elif age >= 55 and age < 65 and coverage_level == "sm":
    driver_data["cost"] = 494
elif age >= 55 and age < 65 and coverage_level == "l":
    driver_data["cost"] = 560
elif age >= 55 and age < 65 and coverage_level == "f":
    driver_data["cost"] = 1363
elif age >= 65 and coverage_level == "sm":
    driver_data["cost"] = 515
elif age >= 65 and coverage_level == "l":
    driver_data["cost"] = 585
elif age >= 65 and coverage_level == "f":
    driver_data["cost"] = 1402

has_customer_been_in_accident = input("Have you been in an accident? (Y/N)")

if has_customer_been_in_accident.lower() == "y":
    driver_data["cost"] = driver_data["cost"] * .41 + driver_data["cost"]

print("The cost for the driver is ${}".format(driver_data["cost"]))
