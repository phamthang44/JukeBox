import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as tkst
import track_library as lib
from track_library import search_Item
from library_item import LibraryItem as libs


def set_text(text_area, content):
    #Inserts content into the text_area
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

def convert_input_number(input):
   #Converts input to integer and validates it
    try:
        track_number = int(input)
    except ValueError:
        messagebox.showerror("Input error", "Please enter a valid input number.")
        return None
    
    if track_number < 1 or track_number > len(lib.library):
        messagebox.showerror("Selection Error", f"Please select a number between 1 and {len(lib.library)}")
        return None

    return track_number

class CreateTrackList:
    def __init__(self, window):
        self.new_window = tk.Toplevel(window)
        self.new_window.title("Create Track List")
        self.new_window.geometry("1920x1080")

        self.selected_tracks = []
        self.text_for_show = ""
        
        # Buttons and Labels
        tk.Button(self.new_window, text="List All Tracks", command=self.list_tracks_clicked).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.new_window, text="Enter Track Number").grid(row=0, column=1, padx=10, pady=10)

        
        
        # Input Fields
        self.input_track_txt = tk.Entry(self.new_window, width=5)
        self.input_track_txt.grid(row=0, column=2, padx=10, pady=10)
        
        self.input_toSearch_txt = tk.Entry(self.new_window, width=5)
        self.input_toSearch_txt.grid(row=2, column=2, padx=10, pady=10)

        # Buttons and Input Areas
        tk.Button(self.new_window, text="Search ID", command=self.search_func).grid(row=3, column=2, padx=10, pady=10)
        tk.Label(self.new_window, text="Enter Number to search").grid(row=2, column=1, padx=10, pady=10)
        
        self.search_ID_txt = tk.Text(self.new_window, width=60, height=5, wrap="none")
        self.search_ID_txt.grid(row=3, column=3, sticky="W", padx=10, pady=10)

        # Control Buttons
        tk.Button(self.new_window, text="Back to main menu", command=self.close_window).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.new_window, text="Add to list", command=self.add_tracks_clicked).grid(row=0, column=3, padx=10, pady=10)
        tk.Button(self.new_window, text="Clear list", command=self.clear_play_list).grid(row=0, column=4, padx=10, pady=10)
        tk.Label(self.new_window, text="Show the tracks with play count").grid(row=4, column=4, padx=10, pady=10)
        tk.Button(self.new_window, text="Play track", command=self.play_track).grid(row=3, column=4, padx=10, pady=10)

        # ScrolledText Areas
        self.list_txt = tkst.ScrolledText(self.new_window, width=48, height=24, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=2, sticky="W", padx=10, pady=10)
        
        self.track_txt = tk.Text(self.new_window, width=45, height=24, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=(50,0), pady=10)

        self.play_count_txt = tk.Text(self.new_window, width=38, height=18)
        self.play_count_txt.grid(row=1, column=4)
        
        self.status_lbl = tk.Label(self.new_window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, sticky="W", padx=10, pady=10)
        
        self.new_window.protocol("WM_DELETE_WINDOW", self.close_window)
        
        self.window = window

    def close_window(self):
        #Close the current window and show the main window
        self.new_window.destroy()
        self.window.deiconify()

        # mai fix - chưa xong 
    def play_track(self):
        #Play the selected tracks          
        self.text_for_show = ""
        for key, track in self.selected_tracks:
            track.increment_play_count() # increase play count by 1           
            show_count = f"ID:{key} {track.name} play count :{track.play_count}\n"
            self.text_for_show += show_count
        set_text(self.play_count_txt, self.text_for_show)
        self.status_lbl.configure(text="All track in selected tracks have been increased by 1!")
            
    def add_tracks_clicked(self):
       #Add track to the selected tracks list
        input_id = self.input_track_txt.get()
        track_number = convert_input_number(input_id)  
        if track_number is None:
            return

        for selected_track_key, selected_track in self.selected_tracks: 
            if int(selected_track_key) == track_number:  
                messagebox.showerror("Duplicate", f"The track {track_number} is already in the list!")
                return
        # if not duplicate, new_track is created to get object by key
        new_track = search_Item(track_number)  # take the track object from track_library func
        if new_track is None:
            messagebox.showerror("Error", f"Track with number {track_number} not found.")
            return
        if new_track:
            self.selected_tracks.append((track_number, new_track))  # add new_track to list selected_tracks
            messagebox.showinfo("Track Added", f"Track {track_number} has been added to the list!")

        track_details = f"{track_number} - {new_track.info()}\n"
        self.text_for_show += track_details

        set_text(self.track_txt, self.text_for_show)
        self.status_lbl.config(text="Track was added to play list!")
# test process a selected_tracks when input already 
    def process_selected_tracks(tracks):
        for key, track in tracks:
            show_play_count = int(track.play_count)
            increase_count = libs.increment_play_count(show_play_count)
            return increase_count    
    
    def list_tracks_clicked(self):
       #Display all tracks in the library
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.config(text="List Tracks button was clicked!")

    def show_info_after_search(self, selected_track, number_check):
        if selected_track:  #check for not None object
            self.text_for_show = f"{selected_track.info()}"
            set_text(self.search_ID_txt, self.text_for_show)
            self.status_lbl.config(text="Search button was clicked!")
        else:
            self.status_lbl.config(text="Track not found.")
            messagebox.showerror("Error", f"Not found the #{number_check} song!")

        # self.text_for_show = f"{} - {selected_track.info()}"
        # set_text(self.search_ID_txt, self.text_for_show)
        # self.status_lbl.config(text="Search button was clicked!")
        
    def search_func(self):
        """Search for a track by track number."""
        input = self.input_toSearch_txt.get()
        track_number = convert_input_number(input)
        if track_number is None:
            messagebox.showerror("Error", f"Track {track_number} not found!")
            return

        for track_key, track in self.selected_tracks:
            if track_number == int(track_key):
                self.show_info_after_search(track, track_number)
                return
        return messagebox.showerror("Error", f"Track {track_number} not found!")

    def clear_play_list(self):
        """Clear the selected tracks list."""
        if not self.selected_tracks:
            return
        self.text_for_show = ""
        self.selected_tracks = []
        set_text(self.track_txt, self.text_for_show)
        self.status_lbl.config(text="Play list was cleared!")








# ---------------------------------------- Draft Area------------------------------------------------------#
        # for track_key, selected_track in lib.library.items():
        #     self.selected_tracks.append((track_key, selected_track))