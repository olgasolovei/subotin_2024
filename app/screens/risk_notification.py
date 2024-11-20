import os
import tkinter as tk
from tkinter import messagebox
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class RiskNotificationScreen:
    def __init__(self, master, on_back):
        self.master = master
        self.on_back = on_back
        master.title("Risk Notification")

        # Create or open the email storage file
        self.email_file_path = "recipient_email.txt"
        self.email_file = open(self.email_file_path, "w")

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
        self.send_button.pack(pady=5)

        # Save Email Button
        self.save_button = tk.Button(master, text="Save Email Address", command=self.save_email_to_file, width=20, height=2)
        self.save_button.pack(pady=5)

        # Back Button
        self.back_button = tk.Button(master, text="Back", command=self.on_back, width=20, height=2)
        self.back_button.pack(pady=5)

        # Close the file when the program closes
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def save_email_to_file(self):
        # Get the email from the entry field
        recipient_email = self.email_entry.get().strip()

        if not recipient_email:
            messagebox.showwarning("Input Error", "Please enter a recipient email address.")
            return

        # Write the email to the file
        self.email_file.seek(0)  # Go to the beginning of the file
        self.email_file.truncate()  # Clear the file
        self.email_file.write(recipient_email)
        self.email_file.flush()  # Ensure it writes immediately
        self.notification_details.config(text="Email address saved!", fg="green")

    def send_notification(self):
        # Get the email from the entry field
        recipient_email = self.email_entry.get().strip()

        if not recipient_email:
            messagebox.showwarning("Input Error", "Please enter a recipient email address.")
            return

        # Prepare the email content
        subject = "Risk Alert: High Wind Speed"
        body = "Warning: High wind speed detected! Risk of crane fall."

        # Send the email
        try:
            self.send_email(recipient_email, subject, body)
            self.notification_details.config(text="Risk notification sent successfully!", fg="green")
        except Exception as e:
            self.notification_details.config(text="Failed to send notification: " + str(e), fg="red")

    def send_email(self, recipient_email, subject, body):
        # Set up SendGrid email message
        message = Mail(
            from_email='your_email@example.com',  # Replace with your SendGrid verified sender email
            to_emails=recipient_email,
            subject=subject,
            plain_text_content=body,
            html_content=f"<h3>{body}</h3>"
        )

        # Send the email using SendGrid API
        try:
            sendgrid_client = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
            response = sendgrid_client.send(message)
            if response.status_code != 202:
                raise Exception(f"Error: {response.status_code} - {response.body}")
        except Exception as e:
            raise Exception("Failed to send email through SendGrid: " + str(e))

    def on_close(self):
        # Close and delete the email file when closing the program
        if self.email_file:
            self.email_file.close()
        if os.path.exists(self.email_file_path):
            os.remove(self.email_file_path)
        self.master.destroy()

# To run the risk notification screen
if __name__ == "__main__":
    root = tk.Tk()
    risk_notification_screen = RiskNotificationScreen(root, lambda: None)
    root.mainloop()
