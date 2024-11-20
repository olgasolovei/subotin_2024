import tkinter as tk
import os
import requests  # Make sure you have the requests library installed
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from tkinter import messagebox

class WeatherForecastScreen:
    def __init__(self, master, on_back, risk_notification_screen):
        self.master = master
        self.on_back = on_back
        self.risk_notification_screen = risk_notification_screen  # Reference to RiskNotificationScreen
        self.setup_ui()

        # Automatically check and send email if needed when the screen loads
        self.check_and_send_warning()

    def setup_ui(self):
        self.master.title("Weather Forecast")

        # Weather Forecast Label
        self.label = tk.Label(self.master, text="Weather Forecast", font=("Arial", 24))
        self.label.pack(pady=10)

        # Current Wind Speed (for demonstration, set a static value or retrieve it dynamically)
        self.wind_speed = 16  # Static value for demonstration, or implement dynamic retrieval here
        self.wind_speed_label = tk.Label(self.master, text=f"Current Wind Speed: {self.wind_speed} m/s", font=("Arial", 16))
        self.wind_speed_label.pack(pady=5)

        # Display Email Notification Address (retrieved from recipient_email.txt)
        self.email_display_label = tk.Label(self.master, text="Notification will be sent to:", font=("Arial", 12))
        self.email_display_label.pack(pady=5)
        self.email_label = tk.Label(self.master, text=self.get_email_from_risk_notification(), font=("Arial", 12), fg="blue")
        self.email_label.pack(pady=5)

        # Back Button
        self.back_button = tk.Button(self.master, text="Back", command=self.on_back, width=20, height=2)
        self.back_button.pack(pady=10)

    def get_email_from_risk_notification(self):
        """Retrieve email address from recipient_email.txt if it exists."""
        email = "No email specified"
        if os.path.exists("recipient_email.txt"):
            with open("recipient_email.txt", "r") as file:
                email = file.read().strip()
        return email

    def check_and_send_warning(self):
        """Check wind speed and send a warning email if it exceeds the threshold."""
        wind_speed_threshold = 15  # Define the threshold for high wind speed

        if self.wind_speed > wind_speed_threshold:
            recipient_email = self.get_email_from_risk_notification()
            if recipient_email and recipient_email != "No email specified":
                try:
                    self.send_email_warning(recipient_email, self.wind_speed)
                    messagebox.showinfo("Notification Sent", "Warning email sent due to high wind speed.")
                except Exception as e:
                    messagebox.showerror("Failed to Send Notification", f"Failed to send email: {e}")

    def send_email_warning(self, recipient_email, wind_speed):
        """Send an email warning via SendGrid."""
        subject = "Risk Alert: High Wind Speed"
        body = f"Warning: High wind speed detected! Current speed is {wind_speed} m/s. Risk of crane fall."

        # Create the email message
        message = Mail(
            from_email="fpace228@gmail.com",  # Replace with your SendGrid sender email
            to_emails=recipient_email,
            subject=subject,
            plain_text_content=body,
            html_content=f"<h3>{body}</h3>"
        )

        # Send the email using SendGrid API
        try:
            sendgrid_client = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))  # Ensure this environment variable is set
            response = sendgrid_client.send(message)
            if response.status_code != 202:
                raise Exception(f"Error: {response.status_code} - {response.body}")
        except Exception as e:
            raise Exception(f"Failed to send email through SendGrid: {e}")
