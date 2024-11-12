import tkinter as tk
from tkinter import messagebox
from helpers import show_message, validate_non_empty  # Assuming you have these functions in helpers.py

class SiteCraneAddScreen:
    def __init__(self, master, on_back):
        self.master = master
        self.on_back = on_back
        master.title("Add Site/Crane")

        # Add Site/Crane Label
        self.label = tk.Label(master, text="Add Site/Crane", font=("Arial", 24))
        self.label.pack(pady=10)

        # Input Fields
        self.site_label = tk.Label(master, text="Site Name:")
        self.site_label.pack()
        self.site_entry = tk.Entry(master)
        self.site_entry.pack(pady=5)

        self.crane_label = tk.Label(master, text="Crane Type:")
        self.crane_label.pack()
        self.crane_entry = tk.Entry(master)
        self.crane_entry.pack(pady=5)

        # Add Button
        self.add_button = tk.Button(master, text="Add", command=self.add_site_crane, width=20, height=2)
        self.add_button.pack(pady=10)

        # Back Button
        self.back_button = tk.Button(master, text="Back", command=self.on_back, width=20, height=2)
        self.back_button.pack(pady=10)

    def add_site_crane(self):
        site_name = self.site_entry.get().strip()  # Trim whitespace
        crane_type = self.crane_entry.get().strip()  # Trim whitespace
        if validate_non_empty(site_name, crane_type):  # Use helper function
            messagebox.showinfo("Success", f"Site '{site_name}' with crane '{crane_type}' added successfully!")
            self.on_back()  # Navigate back to the main screen
        else:
            show_message("Input Error", "Please fill in both fields.")  # Use helper function

# To run the site/crane add screen
if __name__ == "__main__":
    root = tk.Tk()
    site_crane_add_screen = SiteCraneAddScreen(root, lambda: None)
    root.mainloop()