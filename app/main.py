import tkinter as tk
from screens.login_screen import LoginScreen
from screens.main_screen import MainScreen
from screens.weather_forecast import WeatherForecastScreen
from screens.risk_notification import RiskNotificationScreen
from screens.site_crane_add import SiteCraneAddScreen
from screens.user_profile import UserProfileScreen
from screens.password_change import PasswordChangeScreen
from screens.password_recovery import PasswordRecoveryScreen
import os

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Risk Management App")
        self.user_email = None  # Store user email here
        self.risk_notification_screen = None  # Initialize reference to RiskNotificationScreen
        self.show_login_screen()

    def show_login_screen(self):
        self.clear_screen()
        self.login_screen = LoginScreen(self.root, self.show_main_screen)

    def show_main_screen(self):
        self.clear_screen()
        self.main_screen = MainScreen(
            self.root,
            self.show_weather_forecast,
            self.show_user_profile,
            self.show_risk_notification,
            self.show_site_crane_add
        )

    def show_weather_forecast(self):
        self.clear_screen()
        # Ensure risk_notification_screen is initialized
        if self.risk_notification_screen is None:
            self.risk_notification_screen = RiskNotificationScreen(self.root, self.show_main_screen)

        # Pass the initialized RiskNotificationScreen instance to WeatherForecastScreen
        # This allows WeatherForecastScreen to access the email stored in recipient_email.txt
        self.weather_forecast_screen = WeatherForecastScreen(self.root, self.show_main_screen, self.risk_notification_screen)

    def show_risk_notification(self):
        self.clear_screen()
        # Initialize RiskNotificationScreen if not already done and display it
        if self.risk_notification_screen is None:
            self.risk_notification_screen = RiskNotificationScreen(self.root, self.show_main_screen)
        else:
            # Show the already created RiskNotificationScreen
            self.risk_notification_screen.master.lift()

    def show_site_crane_add(self):
        self.clear_screen()
        self.site_crane_add_screen = SiteCraneAddScreen(self.root, self.show_main_screen)

    def show_user_profile(self):
        self.clear_screen()
        self.user_profile_screen = UserProfileScreen(self.root, self.set_user_email, self.show_main_screen)

    def set_user_email(self, email):
        self.user_email = email  # Store email in MainApplication

    def show_password_change(self):
        self.clear_screen()
        self.password_change_screen = PasswordChangeScreen(self.root, self.show_user_profile)

    def show_password_recovery(self):
        self.clear_screen()
        self.password_recovery_screen = PasswordRecoveryScreen(self.root, self.show_login_screen)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
