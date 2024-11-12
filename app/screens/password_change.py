import tkinter as tk
from tkinter import messagebox

class PasswordChangeScreen:
    def __init__(self, master, on_back):
        self.master = master
        self.on_back = on_back
        master.title("Change Password")

        # Change Password Label
        self.label = tk.Label(master, text="Change Password", font=("Arial", 24))
        self.label.pack(pady=10)

        # New Password Input
        self.new_password_label = tk.Label(master, text="New Password:")
        self.new_password_label.pack()
        self.new_password_entry = tk.Entry(master, show='*')
        self.new_password_entry.pack(pady=5)

        # Confirm Password Input
        self.confirm_password_label = tk.Label(master, text="Confirm Password:")
        self.confirm_password_label.pack()
        self.confirm_password_entry = tk.Entry(master, show='*')
        self.confirm_password_entry.pack(pady=5)

        # Change Password Button
        self.change_button = tk.Button(master, text="Change Password", command=self.change_password, width=20, height=2)
        self.change_button.pack(pady=10)

        # Back Button
        self.back_button = tk.Button(master, text="Back", command=self.on_back, width=20, height=2)
        self.back_button.pack(pady=10)

    def change_password(self):
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        if new_password and confirm_password:
            if new_password == confirm_password:
                messagebox.showinfo("Success", "Password changed successfully!")
                self.on_back()  # Navigate back to the user profile screen
            else:
                messagebox.showwarning("Password Mismatch", "Passwords do not match.")
        else:
            messagebox.showwarning("Input Error", "Please fill in both fields.")

# To run the password change screen
if __name__ == "__main__":
    root = tk.Tk()
    password_change_screen = PasswordChangeScreen(root, lambda: None)
    root.mainloop()