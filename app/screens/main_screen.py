import tkinter as tk
from tkinter import messagebox

class MainScreen:
    def __init__(self, master, on_view_forecast, on_view_profile):
        self.master = master
        self.on_view_forecast = on_view_forecast
        self.on_view_profile = on_view_profile
        master.title("Main Screen")

        # Main Menu
        self.label = tk.Label(master, text="Main Menu", font=("Arial", 24))
        self.label.pack(pady=10)

        # Weather Forecast Button
        self.forecast_button = tk.Button(master, text="View Weather Forecast", command=self.on_view_forecast, width=30, height=2)
        self.forecast_button.pack(pady=10)

        # Risk Notification Button
        self.risk_notification_button = tk.Button(master, text="View Risk Notifications", command=self.show_risk_notification, width=30, height=2)
        self.risk_notification_button.pack(pady=10)

        # Add Site/Crane Button
        self.add_site_button = tk.Button(master, text="Add Site/Crane", command=self.show_site_crane_add, width=30, height=2)
        self.add_site_button.pack(pady=10)

        # User Profile Button
        self.profile_button = tk.Button(master, text="User  Profile", command=self.on_view_profile, width=30, height=2)
        self.profile_button.pack(pady=10)

    def show_risk_notification(self):
        # Placeholder for risk notification logic
        messagebox.showinfo("Risk Notification", "Navigating to Risk Notification Screen...")
        self.on_view_forecast()  # Navigate to risk notification screen

    def show_site_crane_add(self):
        # Placeholder for site/crane add logic
        messagebox.showinfo("Add Site/Crane", "Navigating to Add Site/Crane Screen...")
        self.on_view_forecast()  # Navigate to site/crane add screen

# To run the main screen
if __name__ == "__main__":
    root = tk.Tk()
    main_screen = MainScreen(root, lambda: None, lambda: None)
    root.mainloop()