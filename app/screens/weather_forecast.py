import tkinter as tk
from tkinter import messagebox
import requests

class WeatherForecastScreen:
    def __init__(self, master, on_back):
        self.master = master
        self.on_back = on_back
        master.title("Weather Forecast")

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

    def get_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        api_key = "API_KEY"  # Replace with OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_description = data['weather'][0]['description']
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                output = f"Weather in {city}:\n" \
                         f"Description: {weather_description}\n" \
                         f"Temperature: {temperature}°C\n" \
                         f"Humidity: {humidity}%"
                self.weather_output.delete(1.0, tk.END)  # Clear previous output
                self.weather_output.insert(tk.END, output)
            else:
                messagebox.showerror("Error", data.get("message", "Failed to get weather data."))

        except Exception as e:
            messagebox.showerror("Error", str(e))

# To run the weather forecast screen
if __name__ == "__main__":
    root = tk.Tk()
    weather_forecast_screen = WeatherForecastScreen(root, lambda: print("Going back to the previous screen..."))
    root.mainloop()