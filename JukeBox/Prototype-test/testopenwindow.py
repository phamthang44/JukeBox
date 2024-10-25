import tkinter as tk
from tkinter import ttk

# Main Window Class
class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")

        # Main window label
        self.label = ttk.Label(self.root, text="Main Window", font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Button to open new window
        self.open_button = ttk.Button(self.root, text="Open Second Window", command=self.open_second_window)
        self.open_button.pack(pady=10)

    def open_second_window(self):
        self.root.withdraw()  # Hide the main window
        SecondWindow(self.root)  # Open second window and pass the root

# Second Window Class
class SecondWindow:
    def __init__(self, root):
        self.new_window = tk.Toplevel(root)
        self.new_window.title("Second Window")
        
        # Label in second window
        self.label = ttk.Label(self.new_window, text="Second Window", font=("Helvetica", 16))
        self.label.pack(pady=20)
        
        # Button to close and return to main window
        self.close_button = ttk.Button(self.new_window, text="Close and Return to Main", command=self.close_window)
        self.close_button.pack(pady=10)
        
        self.root = root  # Store the reference to the main window (root)

    def close_window(self):
        self.new_window.destroy()  # Close the second window
        self.root.deiconify()  # Show the main window again

# Third Window Class
class ThirdWindow:
    def __init__(self, root):
        self.new_window = tk.Toplevel(root)
        self.new_window.title("Third Window")
        
        # Label in third window
        self.label = ttk.Label(self.new_window, text="Third Window", font=("Helvetica", 16))
        self.label.pack(pady=20)
        
        # Button to close and return to main window
        self.close_button = ttk.Button(self.new_window, text="Close and Return to Main", command=self.close_window)
        self.close_button.pack(pady=10)
        
        self.root = root  # Store the reference to the main window (root)

    def close_window(self):
        self.new_window.destroy()  # Close the third window
        self.root.deiconify()  # Show the main window again

# Create the main window
root = tk.Tk()

# Initialize the MainWindow
main_window = MainWindow(root)

# Start the main loop
root.mainloop()
