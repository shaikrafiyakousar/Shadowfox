"""
ShadowFox Python Development Internship
Task 1 - Topic: If Condition
Author: Shaik Rafiya Kousar
"""

# ---------------------------------------------------------
# 1. BMI Category Calculator
# ---------------------------------------------------------
def bmi_category():
    while True:
        try:
            height = float(input("Enter height in meters: ").strip())
            weight = float(input("Enter weight in kilograms: ").strip())

            if height > 0 and weight > 0:
                break
            print("Height and weight must be positive values.")
        except ValueError:
            print("Please enter valid numeric values.")

    bmi = weight / (height ** 2)

    if bmi >= 30:
        category = "Obesity"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    else:
        category = "Underweight"

    print(f"Your BMI is {bmi:.2f} -> Category: {category}")


# ---------------------------------------------------------
# 2. Determine which country a city belongs to
# ---------------------------------------------------------
australia_cities = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae_cities = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india_cities = ["Mumbai", "Bangalore", "Chennai", "Delhi"]


def find_country(city):
    normalized_city = city.strip().title()
    if normalized_city in australia_cities:
        return "Australia"
    elif normalized_city in uae_cities:
        return "UAE"
    elif normalized_city in india_cities:
        return "India"
    return None


def city_to_country():
    city = input("Enter a city name: ").strip()
    country = find_country(city)

    if country:
        print(f'"{city.title()}" is in {country}')
    else:
        print(f'"{city}" was not found in our records.')


# ---------------------------------------------------------
# 3. Check if two cities belong to the same country
# ---------------------------------------------------------
def compare_cities():
    city1 = input("Enter the first city: ").strip()
    city2 = input("Enter the second city: ").strip()

    country1 = find_country(city1)
    country2 = find_country(city2)

    if country1 and country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")


if __name__ == "__main__":
    print("--- 1. BMI Category ---")
    bmi_category()
    print("\n--- 2. City to Country ---")
    city_to_country()
    print("\n--- 3. Compare Two Cities ---")
    compare_cities()
