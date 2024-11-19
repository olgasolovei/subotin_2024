import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText

class RiskNotificationScreen:
    def __init__(self, master, on_back):
        self.master = master
        self.on_back = on_back
        master.title("Risk Notification")

        # Risk Notification Label
        self.label = tk.Label(master, text="Risk Notifications", font=("Arial", 24))
        self.label.pack(pady=10)

        # Email Entry
        self.email_label = tk.Label(master, text="Enter Recipient Email:")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(master, width=30)
        self.email_entry.pack(pady=5)

        # Notification Details
        self.notification_details = tk.Label(master, text="Risk notifications will be displayed here.", wraplength=400)
        self.notification_details.pack(pady=10)

        # Send Notification Button
        self.send_button = tk.Button(master, text="Send Risk Notification", command=self.send_notification, width=20, height=2)
        self.send_button.pack(pady=10)

        # Back Button
        self.back_button = tk.Button(master, text="Back", command=self.on_back, width=20, height=2)
        self.back_button.pack(pady=10)

        # Variable to store the email
        self.recipient_email = None

    def send_notification(self):
        # Get the email from the entry field
        self.recipient_email = self.email_entry.get().strip()

        if not self.recipient_email:
            messagebox.showwarning("Input Error", "Please enter a recipient email address.")
            return

        # Prepare the email content
        subject = "Risk Alert: High Wind Speed"
        body = "Warning: High wind speed detected! Risk of crane fall."

        # Send the email
        try:
            self.send_email(self.recipient_email, subject, body)
            self.notification_details.config(text="Risk notification sent successfully!", fg="green")
        except Exception as e:
            self.notification_details.config(text="Failed to send notification: " + str(e), fg="red")

    def send_email(self, recipient_email, subject, body):
        sender_email = "fpace228@gmail.com"  # Replace with your email
        sender_password = "Lumino5423"  # Replace with your email password

        # Create the email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

# To run the risk notification screen
if __name__ == "__main__":
    root = tk.Tk()
    risk_notification_screen = RiskNotificationScreen(root, lambda: None)
    root.mainloop()