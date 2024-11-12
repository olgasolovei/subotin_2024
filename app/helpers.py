import re
import tkinter as tk
from tkinter import messagebox

def is_valid_email(email):
    """Validate the email format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_strong_password(password):
    """Check if the password is strong."""
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):  # At least one uppercase letter
        return False
    if not re.search(r"[a-z]", password):  # At least one lowercase letter
        return False
    if not re.search(r"[0-9]", password):  # At least one digit
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # At least one special character
        return False
    return True

def show_message(title, message):
    """Display a message box with a title and message."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo(title, message)
    root.destroy()

def clear_entries(entries):
    """Clear the text entries in a list."""
    for entry in entries:
        entry.delete(0, tk.END)

def validate_non_empty(*args):
    """Check if all provided arguments are non-empty."""
    return all(arg.strip() for arg in args)

# Example usage of the helper functions
if __name__ == "__main__":
    print(is_valid_email("1@1"))  # True
    print(is_strong_password("1"))  # True