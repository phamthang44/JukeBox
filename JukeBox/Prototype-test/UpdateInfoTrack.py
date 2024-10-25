import tkinter as tk
from tkinter import messagebox
from track_library import library_list
import font_manager as fonts

def convert_input_number(input):
        try:
            track_number = int(input) #convert to integer

        except ValueError:
            messagebox.showerror("Input error", "Please enter a valid input number!.")
        if track_number < 0 or track_number > len(library_list):
            messagebox.showerror("Selection Error!", f"Please select a number between 1 and {len(library_list)}")
            return
        return track_number

def set_text(text_area, content):           # inserts content into the text_area
    text_area.delete("1.0", tk.END)         #from 1.0 to end ?
    text_area.insert(1.0, content)
    
class UpdateTrack():

    def __init__(self, window):
        
        self.new_window = tk.Toplevel(window)
        self.new_window.title("Update Track")
        self.new_window.geometry("1150x550")

        # Listbox to display tracks
        self.track_listbox = tk.Listbox(self.new_window, width=50)
        self.track_listbox.pack(pady=10)
        
        # Populate the Listbox with existing tracks
        self.populate_tracks()

        # Entry fields for updating track information
        self.name_entry = tk.Entry(self.new_window )
        self.name_entry.pack(pady=5)

        self.artist_entry = tk.Entry(self.new_window )
        self.artist_entry.pack(pady=5)

        self.rating_entry = tk.Entry(self.new_window )
        self.rating_entry.pack(pady=5)

        # Buttons for updating and deleting
        self.update_button = tk.Button(self.new_window , text="Update Track", command=self.update_track)
        self.update_button.pack(pady=10)

        self.delete_button = tk.Button(self.new_window , text="Delete Track", command=self.delete_track)
        self.delete_button.pack(pady=10)
        
        #back to main menu 
        self.back_button = tk.Button(self.new_window , text="Back to main menu", command=self.close_window)
        self.back_button.pack(pady=10)
        

        # Bind the selection event to load track details
        self.track_listbox.bind("<<ListboxSelect>>", self.load_track_details)
        
        self.window = window
    
    def search_func(self):
        selected_tracks = []
        
        input = self.input_toSearch_txt.get()
        track_number = convert_input_number(input)
        
        if track_number <= 0 or track_number > len(library_list):
            return "Not Found!"
        
        selected_tuple = library_list[track_number - 1] # Access by index
        int_key, selected_track = selected_tuple
        

        selected_tracks.append((int_key, selected_track))
        
        
        track_details = f"{int_key} - {selected_track.info()}"
        self.text_for_show =  track_details
        
        if len(selected_tracks) <= 0:   # this is how you test if the list is empty
            return "Not Found!"
                         # we'll use this as index to traverse the list
        for track_tuple in selected_tracks:
            if track_tuple[0] == track_number:  # Compare int_key with track_number (key, value) track_tuple[0] ~ key list[1]  
                set_text(self.search_ID_txt, self.text_for_show)
                self.status_lbl.configure(text="Search button was clicked!")
                return "Found!"
        else:               # this executes only if the loop didn't find the element
            return "failure"   
    
    def close_window(self):
        self.new_window.destroy()  # hide this current window
        self.window.deiconify()  #back to main menu
    
    def populate_tracks(self):
        """ Populate the Listbox with track titles. """
        self.track_listbox.delete(0, tk.END)  # Clear existing entries
        for index, item in library_list:
            self.track_listbox.insert(tk.END, f"{item.info()}")

    def load_track_details(self, event):
        """ Load selected track details into entry fields. """
        selection = self.track_listbox.curselection()
        
        if selection:
            index = selection[0]
            track_key, track = library_list[index]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, track.name)
            self.artist_entry.delete(0, tk.END)
            self.artist_entry.insert(0, track.artist)
            self.rating_entry.delete(0, tk.END)
            self.rating_entry.insert(0, track.rating)

    def update_track(self):
        """ Update the selected track's information. """
        selection = self.track_listbox.curselection()
        if not selection:
            messagebox.showerror("Selection Error", "Please select a track to update.")
            return
    
        index = selection[0]
        new_name = self.name_entry.get()
        new_artist = self.artist_entry.get()
        new_rating = self.rating_entry.get()

        # Validate new rating (example: should be an integer between 0 and 5)
        try:
            new_rating = int(new_rating)
            if new_rating < 0 or new_rating > 5:
                raise ValueError("Rating must be between 0 and 5.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid rating between 0 and 5.")
            return
        #unpack the library_list because library_list is a tuple (int_key, value) before .
        track_key, track_object = library_list[index]
        #now is track_key similar to int_key and track_object similar to LibraryItem() object 
        # Update the track information
        track_object.name = new_name
        track_object.artist = new_artist
        track_object.rating = new_rating

        messagebox.showinfo("Success", "Track updated successfully.")
        self.populate_tracks()  # Refresh the Listbox

    def delete_track(self):
        """ Delete the selected track. """
        selection = self.track_listbox.curselection()
        if not selection:
            messagebox.showerror("Selection Error", "Please select a track to delete.")
            return

        index = selection[0]
        confirmation = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this track?")
        if confirmation:
            del library_list[index]  # Remove the track from the list
            messagebox.showinfo("Success", "Track deleted successfully.")
            self.populate_tracks()  # Refresh the Listbox

#------------------------ Test ---------------------------

# if __name__ == "__main__":
#     new_window = tk.Tk()
#     fonts.configure()
#     UpdateTrack(new_window)
#     new_window.mainloop()

        # self.input_toSearch_txt = tk.Entry(self.new_window, width=5)              #the box to entry
        # self.input_toSearch_txt.pack(pady=10)
        # #search button
        # search_btn = tk.Button(self.new_window, text="Search ID ", command=self.search_func)
        # search_btn.pack(pady=10)
        # #label 
        
        # update_btn = tk.Button(self.new_window, text="Update track", command=self.update_track)
        # update_btn.pack(pady=10)
        # #label 
        