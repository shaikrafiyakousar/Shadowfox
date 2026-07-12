"""
ShadowFox Python Development Internship
Task 1 - Topic: Dictionary
Author: Shaik Rafiya Kousar
"""

# ---------------------------------------------------------
# 1. List of friends' names -> list of tuples (name, length of name)
# ---------------------------------------------------------
friends = ["Sadiya", "Naziya", "Johiya", "Navya", "Rayyan"]
friends_with_length = [(name, len(name)) for name in friends]

print("1. Friends with name length:")
print(friends_with_length)
print()


# ---------------------------------------------------------
# 2. Trip expense tracker
# ---------------------------------------------------------
your_expenses = {
    "Hotel": 1100,
    "Food": 750,
    "Transportation": 450,
    "Attractions": 350,
    "Miscellaneous": 180
}

partner_expenses = {
    "Hotel": 1300,
    "Food": 700,
    "Transportation": 500,
    "Attractions": 250,
    "Miscellaneous": 220
}

total_yours = sum(your_expenses.values())
total_partner = sum(partner_expenses.values())

print("2. Trip Expense Summary")
print("Your total expenses:", total_yours)
print("Partner's total expenses:", total_partner)

if total_yours > total_partner:
    print("You spent more money overall.")
elif total_partner > total_yours:
    print("Your partner spent more money overall.")
else:
    print("Both of you spent the same amount overall.")

# Find category with the biggest difference in spending
biggest_diff_category = None
biggest_diff = 0

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > biggest_diff:
        biggest_diff = diff
        biggest_diff_category = category

print(f"Biggest spending difference is in '{biggest_diff_category}' category: {biggest_diff}")
