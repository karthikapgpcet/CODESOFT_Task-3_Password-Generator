import tkinter as tk
from tkinter import ttk
import random

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.create_widgets()

    def create_widgets(self):
        # Password Length Label and Entry
        length_label = ttk.Label(self.master, text="Password Length:")
        length_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.length_entry = ttk.Entry(self.master, width=10)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Password Complexity Label and Combobox
        complexity_label = ttk.Label(self.master, text="Password Complexity:")
        complexity_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.complexity_combobox = ttk.Combobox(self.master, values=["Weak", "Strong", "Very Strong"])
        self.complexity_combobox.set("Strong")  # Default to "Strong"
        self.complexity_combobox.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        # Generate Password Button
        generate_button = ttk.Button(self.master, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Display Generated Password Label
        self.password_label = ttk.Label(self.master, text="")
        self.password_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        try:
            # Get password length from the entry
            length = int(self.length_entry.get())

            # Validate the length
            if length <= 0:
                self.password_label.config(text="Invalid length. Please enter a positive integer.")
                return

            # Get complexity choice from the combobox
            complexity = self.complexity_combobox.get()

            # Generate the password based on complexity
            password = self._generate_password(length, complexity)

            # Display the generated password
            self.password_label.config(text=f"Generated Password: {password}")

        except ValueError:
            self.password_label.config(text="Invalid input. Please enter a valid integer for the password length.")
        except Exception as e:
            self.password_label.config(text=f"An error occurred: {e}")

    def _generate_password(self, length, complexity):
        # Define character sets for password generation
        lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        special_characters = "!@#$%^&*_/"

        # Combine character sets based on complexity
        if complexity == "Weak":
            characters = lowercase_letters + uppercase_letters
        elif complexity == "Strong":
            characters = lowercase_letters + digits + uppercase_letters
        elif complexity == "Very Strong":
            characters = lowercase_letters + uppercase_letters + digits + special_characters
        else:
            raise ValueError("Invalid complexity choice")

        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

# Main application
root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()
