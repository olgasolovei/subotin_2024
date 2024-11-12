import tkinter as tk
from tkinter import messagebox

class LoginScreen:
    def __init__(self, master, on_login_success):
        self.master = master
        self.on_login_success = on_login_success
        master.title("Login")

        # Background
        master.configure(bg='lightgray')

        # Logo
        logo = tk.Label(master, text="Company Logo", bg='lightgray', font=("Arial", 24))
        logo.pack(pady=10)

        # Login Input
        self.login_label = tk.Label(master, text="Login:", bg='lightgray')
        self.login_label.pack()
        self.login_entry = tk.Entry(master)
        self.login_entry.pack(pady=5)

        # Password Input
        self.password_label = tk.Label(master, text="Password:", bg='lightgray')
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show='*')
        self.password_entry.pack(pady=5)

        # Login Button
        self.login_button = tk.Button(master, text="Login", command=self.login, bg='blue', fg='white', width=20, height=2)
        self.login_button.pack(pady=10)

        # Forgot Password Link
        self.forgot_password_link = tk.Label(master, text="Forgot password?", bg='lightgray', fg='blue', cursor='hand2')
        self.forgot_password_link.pack(pady=5)
        self.forgot_password_link.bind("<Button-1>", self.forgot_password)

    def login(self):
        # Placeholder for login logic
        username = self.login_entry.get()
        password = self.password_entry.get()
        if username and password:
            messagebox.showinfo("Login", "Login successful!")
            self.on_login_success()  # Call the success callback
        else:
            messagebox.showwarning("Login", "Please enter both fields.")

    def forgot_password(self, event):
        self.on_login_success()  # Navigate to the password recovery screen

# To run the login screen
if __name__ == "__main__":
    root = tk.Tk()
    login_screen = LoginScreen(root, lambda: None)
    root.mainloop()