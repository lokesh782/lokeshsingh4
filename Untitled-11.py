# Input: Ask the user for the current weather
weather = input("What is the weather like today? (sunny/rainy): ").strip().lower()

# Activity suggestion based on weather
if weather == 'sunny':
    print("The weather is sunny! How about going for a hike or having a picnic?")
elif weather == 'rainy':
    # Input: Check if the user has a raincoat or umbrella
    has_raincoat_umbrella = input("Do you have a raincoat or umbrella? (yes/no): ").strip().lower()
    
    if has_raincoat_umbrella == 'yes':
        print("You can go to a nearby mall or museum!")
    else:
        print("It's best to stay home and watch movies today.")
else:
    print("Sorry, I didn't recognize that weather. Please enter 'sunny' or 'rainy'.")
