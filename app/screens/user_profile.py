import tkinter as tk
from tkinter import messagebox
from helpers import show_message  # Assuming you have a show_message function in helpers.py

class UserProfileScreen:
    def __init__(self, master, on_back):
        self.master = master
        self.on_back = on_back
        master.title("User  Profile")

        # User Profile Label
        self.label = tk.Label(master, text="User  Profile", font=("Arial", 24))
        self.label.pack(pady=10)

        # User Information (Example)
        self.username_label = tk.Label(master, text="Username: user123")
        self.username_label.pack(pady=5)

        # Change Password Button
        self.change_password_button = tk.Button(master, text="Change Password", command=self.change_password, width=20, height=2)
        self.change_password_button.pack(pady=10)

        # Back Button
        self.back_button = tk.Button(master, text="Back", command=self.on_back, width=20, height=2)
        self.back_button.pack(pady=10)

    def change_password(self):
        # Logic to change the password
        # This could open a new window or prompt for a new password
        show_message("Change Password", "This would open the change password dialog.")

# To run the user profile screen
if __name__ == "__main__":
    root = tk.Tk()
    user_profile_screen = UserProfileScreen(root, lambda: print("Going back to the previous screen..."))
    root.mainloop()