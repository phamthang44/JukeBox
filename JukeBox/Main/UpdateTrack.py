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
    #Class to handle track updates based on ID
    
    def __init__(self, window):
        self.new_window = tk.Toplevel(window)
        self.new_window.title("Update Track")
        self.new_window.geometry("1150x550")
        self.csv_path = r'JukeBox\Main\data.csv'
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
        #Close the current window and return to the main window
        self.new_window.destroy()
        self.window.deiconify()

    def find_track_by_id(self, track_id):  
        #Find and return a track by its ID      
        for track_key, track_object in lib.library.items(): #return the track in lib.library.items() -> dict_items([("01", LibraryItems(.....)), (tuple2),..])    track_key -> "01" and track_object will be LibraryItem(.....)
            if int(track_key) == track_id:  # If ID matches
                return track_object
        return None

    def load_track_by_id(self):
        #Load track details into the labels based on the ID
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
        track_id_str = f"0" + str(track_id) # when combine f" "0" + str(track_id) 
                                            # ex : track_id = 1 -> track_id_str will be "01" as a string like the key in dict library
        
        if track_id_str in library:  # check the key if in library will update the new_rating on screen and also on data.csv
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
            data = list(reader)  #loads all rows from the CSV into a list called data, where each row is represented as a list of strings.

    # Update the row corresponding to the track_id
        for i, row in enumerate(data):
            if row[0] == track_id:
                current_track = library[track_id]  # Get the updated LibraryItem
                data[i] = [track_id, current_track.name, current_track.artist, current_track.rating, current_track.youtube_link, current_track.duration]  # Update the row
                break
            #data[i] refers to a specific row in data list 
            #The line data[i] is used to access the specific row in the data list that you want to update.
            #row[0] means the first element in the inner list1 "01" in list data[]
            #summary data will like this data = [[inner list1], [inner list2]]
            #Each inner list (representing a row) contains multiple elements
        
        #"For each row in the data list, I want to do something. Also, while I do this, keep track of the row's position in the list, starting from zero."
        
            
    # Write the updated data back to the CSV
        with open(self.csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)  # Write all rows back to the file
            
            
            
        #The purpose of this function is to:
        #1 Load the contents of a CSV file into a list.
        #2 Update the row in that list corresponding to the given track_id with the current details of the LibraryItem.
        #3 Write the updated list back to the CSV file.
        
        # for example view of data list
# data = [
#     ['01', 'Shape of You', 'Ed Sheeran', '5'],  # First track    
#     ['02', 'Perfect', 'Ed Sheeran', '4'],       # Second track
#     ['03', 'Blinding Lights', 'The Weeknd', '5']  # Third track
# ]        
        
 
                                        
        
        
        
        
        
#------------------------ Test the UpdateTrack class ---------------------------
# Uncomment the following to test the functionality independently
# if __name__ == "__main__":
#     root = tk.Tk()
#     fonts.configure()
#     UpdateTrack(root)
#     root.mainloop()
