# Weather-Based Outfit Advisor
# Author: [Your Name]
# Date: [Today's Date]
# Description:
# This program suggests an outfit based on the user's input of temperature, weather type, and wind speed.

def get_temperature():
    while True:
        try:
            temp = float(input("Enter the current temperature (°F): "))
            if -50 <= temp <= 130:
                return temp
            print("Please enter a realistic temperature between -50 and 130 °F.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_weather_type():
    valid_types = ["sunny", "rainy", "snowy", "cloudy", "windy"]
    while True:
        weather = input("Enter the weather type (sunny, rainy, snowy, cloudy, windy): ").lower()
        if weather in valid_types:
            return weather
        print("Invalid weather type. Please choose from sunny, rainy, snowy, cloudy, or windy.")

def get_wind_speed():
    while True:
        try:
            wind = float(input("Enter the wind speed (mph): "))
            if 0 <= wind <= 100:
                return wind
            print("Please enter a realistic wind speed between 0 and 100 mph.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def suggest_outfit(temp, weather, wind):
    print("\n=== Outfit Suggestion ===")
    # Cold and windy
    if temp < 40 and wind > 15:
        print("It's cold and windy. Wear a heavy coat, scarf, gloves, and boots.")
    # Cold but not too windy
    elif temp < 40:
        print("It's cold. Wear a warm coat, hat, and layers.")
    # Cool and sunny
    elif 40 <= temp <= 70 and weather == "sunny":
        print("It's cool and sunny. A light jacket and jeans will be perfect.")
    # Cool and rainy
    elif 40 <= temp <= 70 and weather == "rainy":
        print("It's cool and rainy. Wear a waterproof jacket and boots.")
    # Warm and sunny
    elif temp > 70 and weather == "sunny":
        print("It's warm and sunny. Wear shorts, a t-shirt, and sunglasses.")
    # Warm and rainy
    elif temp > 70 and weather == "rainy":
        print("It's warm and rainy. A t-shirt and light raincoat should do.")
    # Snowy
    elif weather == "snowy":
        print("It's snowy. Wear a thick coat, boots, gloves, and a hat.")
    # Cloudy and moderate
    elif weather == "cloudy" and 50 <= temp <= 75:
        print("It's cloudy. A hoodie or sweater should be fine.")
    # Default case
    else:
        print("Dress in layers and check local updates just to be safe.")

def main():
    print("=== Weather-Based Outfit Advisor ===")

    # Get validated inputs
    temperature = get_temperature()
    weather_type = get_weather_type()
    wind_speed = get_wind_speed()

    # Suggest an outfit
    suggest_outfit(temperature, weather_type, wind_speed)

# Run the program
if __name__ == "__main__":
    main()
