# Gardening advice app

def gardening_tip(month):

    if month == "December":
        return "Water plants regularly because it is summer."

    elif month == "June":
        return "Protect plants from frost during winter."

    elif month == "September":
        return "Spring is perfect for planting flowers."

    else:
        return "Check seasonal gardening tips."


month = "May"

print(gardening_tip(month))
=======
# TODO:
# Create functions to avoid repeating code
# Add more comments/documentation
# Replace hardcoded month names with variables

month = "May"

if month == "December":
    print("Water plants regularly because it is summer.")

elif month == "June":
    print("Protect plants from frost during winter.")

elif month == "September":
    print("Spring is perfect for planting flowers.")

else:
    print("Check seasonal gardening tips.")
>>>>>>> a26fcd3a5e2acedcc8122399ba165f5ec002aebb
