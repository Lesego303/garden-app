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