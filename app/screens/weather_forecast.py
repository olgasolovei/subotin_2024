import tkinter as tk
from tkinter import messagebox
import random
import sqlite3

class WeatherForecastScreen:
    def __init__(self, master, on_back):
        self.master = master
        self.on_back = on_back
        master.title("Weather Forecast")

        # Database setup
        self.conn = self.setup_database()

        # Weather Label
        self.label = tk.Label(master, text="Weather Forecast", font=("Arial", 24))
        self.label.pack(pady=10)

        # City Input
        self.city_label = tk.Label(master, text="Enter City:")
        self.city_label.pack()
        self.city_entry = tk.Entry(master)
        self.city_entry.pack(pady=5)

        # Get Weather Button
        self.get_weather_button = tk.Button(master, text="Get Weather", command=self.get_weather, width=20, height=2)
        self.get_weather_button.pack(pady=10)

        # Weather Output
        self.weather_output = tk.Text(master, height=10, width=50)
        self.weather_output.pack(pady=10)

        # Back Button
        self.back_button = tk.Button(master, text="Back", command=self.on_back, width=20, height=2)
        self.back_button.pack(pady=10)

    def setup_database(self):
        conn = sqlite3.connect('weather_forecast.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                temperature REAL,
                humidity REAL,
                wind_speed REAL
            )
        ''')
        conn.commit()
        return conn

    def generate_weather_data(self, city):
        temperature = random.randint(-10, 5)  # Temperature in Celsius (winter range)
        humidity = random.randint(60, 100)  # Humidity percentage
        wind_speed = random.uniform(10, 20)  # Wind speed in m/s
        return city, temperature, humidity, wind_speed

    def insert_weather_data(self, city, temperature, humidity, wind_speed):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO weather (city, temperature, humidity, wind_speed)
            VALUES (?, ?, ?, ?)
        ''', (city, temperature, humidity, wind_speed))
        self.conn.commit()

    def check_wind_speed(self, wind_speed):
        if wind_speed > 15:
            return "Warning: High wind speed! Risk of crane fall."
        return ""

    def get_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        city, temperature, humidity, wind_speed = self.generate_weather_data(city)

        self.insert_weather_data(city, temperature, humidity, wind_speed)
        risk_message = self.check_wind_speed(wind_speed)

        output = f"Weather in {city}:\n" \
                 f"Temperature: {temperature}°C\n" \
                 f"Humidity: {humidity}%\n" \
                 f"Wind Speed: {wind_speed:.2f} m/s\n"

        if risk_message:
            output += risk_message + "\n"

        self.weather_output.delete(1.0, tk.END)  # Clear previous output
        self.weather_output.insert(tk.END, output)

    def on_closing(self):
        self.conn.close()
        self.master.destroy()

# To run the weather forecast screen
if __name__ == "__main__":
    root = tk.Tk()
    weather_forecast_screen = WeatherForecastScreen(root, lambda: print("Going back to the previous screen..."))
    root.protocol("WM_DELETE_WINDOW", weather_forecast_screen.on_closing)  # Ensure database closes on exit
    root.mainloop()