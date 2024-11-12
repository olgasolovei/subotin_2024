import tkinter as tk
from tkinter import messagebox

class RiskNotificationScreen:
    def __init__(self, master, on_back):
        self.master = master
        self.on_back = on_back
        master.title("Risk Notification")

        # Risk Notification Label
        self.label = tk.Label(master, text="Risk Notifications", font=("Arial", 24))
        self.label.pack(pady=10)

        # Notification Details
        self.notification_details = tk.Label(master, text="Risk notifications will be displayed here.", wraplength=400)
        self.notification_details.pack(pady=10)

        # Back Button
        self.back_button = tk.Button(master, text="Back", command=self.on_back, width=20, height=2)
        self.back_button.pack(pady=10)

# To run the risk notification screen
if __name__ == "__main__":
    root = tk.Tk()
    risk_notification_screen = RiskNotificationScreen(root, lambda: None)
    root.mainloop()