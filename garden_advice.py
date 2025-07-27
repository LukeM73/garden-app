# Dictionary of plants by season (New feature)
SEASONAL_PLANTS = {
    "summer": ["Sunflowers", "Tomatoes", "corn"],
    "winter": ["Pansies", "Kale", "Brussels Sprouts"]
}

def get_seasonal_plants(season):
    """Return a list of plants recommended for the given season."""
    return SEASONAL_PLANTS.get(season.lower(), ["No seasonal plants found"])

# Hardcoded values for the season and plant type
print('''All the seasons we can give advice for!
        1. Summer
        2. Winter''')
print('''All the plant types we can give advice for!
        1. Flowers
        2. Vegetables
        ''')

season = input("Enter which season you would like advice for... 'Summer' or 'Winter': ").lower()
plant_type = input("Enter the plant type you would like advice for... 'Flower' or 'Vegetable': ").lower()

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Get seasonal plant recommendations (New feature)
plants = get_seasonal_plants(season)
advice += f"\nRecommended plants for {season.capitalize()}: {', '.join(plants)}\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)
