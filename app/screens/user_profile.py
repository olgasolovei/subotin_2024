import tkinter as tk
from tkinter import messagebox
from helpers import show_message  # Assuming you have a show_message function in helpers.py

class UserProfileScreen:
    def __init__(self, master, set_user_email, on_back):
        self.master = master
        self.set_user_email = set_user_email
        self.on_back = on_back
        master.title("User  Profile")

        # User Profile Label
        self.label = tk.Label(master, text="User  Profile", font=("Arial", 24))
        self.label.pack(pady=10)

        # User Information (Example)
        self.username_label = tk.Label(master, text="Username: user123")
        self.username_label.pack(pady=5)

        # Email Entry
        self.email_label = tk.Label(master, text="Email:")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(master)
        self.email_entry.pack(pady=5)

        # Save Email Button
        self.save_email_button = tk.Button(master, text="Save Email", command=self.save_email, width=20, height=2)
        self.save_email_button.pack(pady=10)

        # Change Password Button
        self.change_password_button = tk.Button(master, text="Change Password", command=self.change_password, width=20, height=2)
        self.change_password_button.pack(pady=10)

        # Back Button
        self.back_button = tk.Button(master, text="Back", command=self.on_back, width=20, height=2)
        self.back_button.pack(pady=10)

    def save_email(self):
        email = self.email_entry.get()
        self.set_user_email(email)  # Store email in MainApplication
        messagebox.showinfo("Email Saved", f"Email saved: {email}")

    def change_password(self):
        # Logic to change the password
        show_message("Change Password", "This would open the change password dialog.")

# To run the user profile screen
if __name__ == "__main__":
    root = tk.Tk()
    user_profile_screen = UserProfileScreen(root, lambda email: print(f"Email set: {email}"), lambda: print("Going back to the previous screen..."))
    root.mainloop()