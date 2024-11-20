import tkinter as tk

class MainScreen:
    def __init__(self, master, on_view_forecast, on_view_profile, on_view_risk_notification, on_add_site_crane):
        self.master = master
        self.on_view_forecast = on_view_forecast
        self.on_view_profile = on_view_profile
        self.on_view_risk_notification = on_view_risk_notification
        self.on_add_site_crane = on_add_site_crane
        master.title("Main Screen")

        # Weather Forecast Button
        self.forecast_button = tk.Button(master, text="View Weather Forecast", command=self.on_view_forecast, width=30, height=2)
        self.forecast_button.pack(pady=10)

        # Risk Notification Button
        self.risk_notification_button = tk.Button(master, text="View Risk Notifications", command=self.on_view_risk_notification, width=30, height=2)
        self.risk_notification_button.pack(pady=10)

        # Add Site/Crane Button
        self.add_site_button = tk.Button(master, text="Add Site/Crane", command=self.on_add_site_crane, width=30, height=2)
        self.add_site_button.pack(pady=10)

        # User Profile Button
        self.profile_button = tk.Button(master, text="User Profile", command=self.on_view_profile, width=30, height=2)
        self.profile_button.pack(pady=10)
