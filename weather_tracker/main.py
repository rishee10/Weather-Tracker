# main.py

from weather_utils import fetch_weather

def main():
    cities = []
    print("Enter city names (type 'done' to finish):")
    while True:
        city = input("City: ").strip()
        if city.lower() == "done":
            break
        if city:
            cities.append(city)

    print("\nWeather Report:")
    print("-" * 120)

    for city in cities:
        weather = fetch_weather(city)
        if weather:
            print(weather)
            print("-" * 120)

if __name__ == "__main__":
    main()
