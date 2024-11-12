import tkinter as tk
from tkinter import messagebox

class PasswordRecoveryScreen:
    def __init__(self, master, on_back):
        self.master = master
        self.on_back = on_back
        master.title("Password Recovery")

        # Password Recovery Label
        self.label = tk.Label(master, text="Password Recovery", font=("Arial", 24))
        self.label.pack(pady=10)

        # Email Input
        self.email_label = tk.Label(master, text="Enter your email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(master)
        self.email_entry.pack(pady=5)

        # Recover Button
        self.recover_button = tk.Button(master, text="Recover Password", command=self.recover_password, width=20, height=2)
        self.recover_button.pack(pady=10)

        # Back Button
        self.back_button = tk.Button(master, text="Back", command=self.on_back, width=20, height=2)
        self.back_button.pack(pady=10)

    def recover_password(self):
        email = self.email_entry.get()
        if email:
            messagebox.showinfo("Recovery", f"Recovery instructions sent to {email}.")
            self.on_back()  # Navigate back to the login screen
        else:
            messagebox.showwarning("Input Error", "Please enter your email.")

# To run the password recovery screen
if __name__ == "__main__":
    root = tk.Tk()
    password_recovery_screen = PasswordRecoveryScreen(root, lambda: None)
    root.mainloop()