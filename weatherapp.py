import tkinter as tk
import requests
from tkinter import messagebox

def get_weather_data():
    city = city_entry.get()
    if city:
        api_key = 'af393fcfb2e244c7a5b51329231310'
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        response = requests.get(url)

        if response.status_code == 200:
            data = eval(response.text)  # Using eval to parse the string

            # Extracting weather data
            location = data['location']['name']
            country = data['location']['country']
            temp_c = data['current']['temp_c']
            temp_f = data['current']['temp_f']
            condition = data['current']['condition']['text']
            humidity = data['current']['humidity']
            wind_speed = data['current']['wind_kph']

            # Display weather details
            result_label.config(text=f"Weather in {location}, {country}:\n"
                                     f"Temperature: {temp_c}°C / {temp_f}°F\n"
                                     f"Condition: {condition}\n"
                                     f"Humidity: {humidity}%\n"
                                     f"Wind Speed: {wind_speed} km/h")
        else:
            messagebox.showerror("Error", "Failed to retrieve data. Check the city name.")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# GUI setup
root = tk.Tk()
root.title("Weather App")

# Label and entry for city input
city_label = tk.Label(root, text="Enter City Name:", font=("Helvetica", 12))
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Button to fetch weather data
fetch_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12), command=get_weather_data)
fetch_button.pack(pady=10)

# Label to display weather information
result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()

