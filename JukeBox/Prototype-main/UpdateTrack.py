import tkinter as tk
from tkinter import messagebox
from library_item import LibraryItem
import track_library as lib
from track_library import library
import font_manager as fonts
import csv
import io
import sys

def convert_input_number(input):
    """Convert the input string to an integer and check if it's valid."""
    try:
        track_number = int(input)  # Convert input to integer
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number!")
        return None
    
    if track_number < 0 or track_number > len(lib.library):
        messagebox.showerror("Selection Error", f"Please select a number between 1 and {len(lib.library)}.")
        return None
    
    return track_number

class UpdateTrack:
    """Class to handle track updates based on ID."""
    
    def __init__(self, window):
        self.new_window = tk.Toplevel(window)
        self.new_window.title("Update Track")
        self.new_window.geometry("1150x550")
        self.csv_path = 'D:\Desktop\GCS230575 - Python OOP\Coursework-main\JukeBox\Prototype-main\data.csv'
        # Entry for ID
        self.id_entry = tk.Entry(self.new_window, width=20)
        self.id_entry.pack(pady=5)
        self.id_label = tk.Label(self.new_window, text="Enter Track ID to Load Info:")
        self.id_label.pack()

        # Load Info button
        self.load_button = tk.Button(self.new_window, text="Load Info", command=self.load_track_by_id)
        self.load_button.pack(pady=10)

        # Fields for displaying and updating track information
        self.name_label = tk.Label(self.new_window, text="Track Name:")
        self.name_label.pack()
        self.name_value = tk.Label(self.new_window, text="", width=40, relief=tk.SUNKEN)
        self.name_value.pack(pady=5)

        self.artist_label = tk.Label(self.new_window, text="Artist:")
        self.artist_label.pack()
        self.artist_value = tk.Label(self.new_window, text="", width=40, relief=tk.SUNKEN)
        self.artist_value.pack(pady=5)

        self.current_rating_label = tk.Label(self.new_window, text="Current Rating:")
        self.current_rating_label.pack()
        self.current_rating_value = tk.Label(self.new_window, text="", width=10, relief=tk.SUNKEN)
        self.current_rating_value.pack(pady=5)

        # Entry field for new rating
        self.rating_entry = tk.Entry(self.new_window)
        self.rating_entry.pack(pady=5)
        self.rating_label = tk.Label(self.new_window, text="Enter New Rating (0-5):")
        self.rating_label.pack()

        # Update button
        self.update_button = tk.Button(self.new_window, text="Update Track Rating", command=self.update_track_by_id)
        self.update_button.pack(pady=10)
        
        # Back to Main Menu Button
        self.back_button = tk.Button(self.new_window, text="Back to Main Menu", command=self.close_window)
        self.back_button.pack(pady=10)
        
        self.new_window.protocol("WM_DELETE_WINDOW", self.close_window)
        
        self.current_track = None  # To store the currently loaded track
        self.window = window

    def close_window(self):
        """Close the current window and return to the main window."""
        self.new_window.destroy()
        self.window.deiconify()

    def find_track_by_id(self, track_id):
        """Find and return a track by its ID."""
        for track_key, track_object in lib.library.items():
            if int(track_key) == track_id:  # If ID matches
                return track_object
        return None

    def load_track_by_id(self):
        """Load track details into the labels based on the ID."""
        # Get track ID from user input
        track_id_input = self.id_entry.get()
        track_id = convert_input_number(track_id_input)
        
        if track_id is None:
            return  # Invalid input

        # Find the track with the given ID
        track_object = self.find_track_by_id(track_id)
        
        if track_object is None:
            messagebox.showerror("Track Not Found", "No track found with the given ID.")
            return

        # Display the track details in the labels
        self.name_value.config(text=track_object.name)
        self.artist_value.config(text=track_object.artist)
        self.current_rating_value.config(text=str(track_object.rating))
        
        # Store the current track object for future updates
        self.current_track = track_object

    def update_track_by_id(self):
        track_id_input = self.id_entry.get()
        track_id = convert_input_number(track_id_input)
        """Update the track's rating based on the current loaded track."""
        if self.current_track is None:
            messagebox.showerror("No Track Loaded", "Please load a track by entering its ID first.")
            return

        # Get new rating from user input
        new_rating_input = self.rating_entry.get()
        
        # Validate new rating (should be an integer between 0 and 5)
        try:
            new_rating = int(new_rating_input)
            if new_rating < 0 or new_rating > 5:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid rating between 0 and 5.")
            return

        # Update the current track's rating
        track_id_str = f"0" + str(track_id)
        
        if track_id_str in library:
            library[track_id_str].rating = new_rating
            self.current_track.rating = new_rating
            self._update_csv(track_id_str)
            messagebox.showinfo("Success", f"Track ID {track_id} rating updated to {new_rating}.")        
            self.current_rating_value.config(text=str(new_rating))
        else:
            messagebox.showerror("Error", f"Track ID {track_id} not found in the library")
 
    def _update_csv(self, track_id):
        with open(self.csv_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)  # Load all rows into a list

    # Update the row corresponding to the track_id
        for i, row in enumerate(data):
            if row[0] == track_id:
                current_track = library[track_id]  # Get the updated LibraryItem
                data[i] = [track_id, current_track.name, current_track.artist, current_track.rating]  # Update the row
                break

    # Write the updated data back to the CSV
        with open(self.csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)  # Write all rows back to the file
        

            
#------------------------ Test the UpdateTrack class ---------------------------
# Uncomment the following to test the functionality independently
# if __name__ == "__main__":
#     root = tk.Tk()
#     fonts.configure()
#     UpdateTrack(root)
#     root.mainloop()
