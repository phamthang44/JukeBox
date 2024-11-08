import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as tkst
import track_library as lib
from track_library import search_Item
from library_item import LibraryItem as libs
import webbrowser

def set_text(text_area, content):
    #Inserts content into the text_area
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)
@staticmethod
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
        self.new_window.geometry("1600x800")

        self.selected_tracks = []
        self.text_for_show = ""
        self.track_lists = {} 
        self.index = 0
        self.is_playing = False
        
        self.initUI()
        self.new_window.protocol("WM_DELETE_WINDOW", self.close_window)
        self.list_tracks_clicked()
        self.window = window

    def initUI(self):
        # Buttons and Labels
        tk.Button(self.new_window, text="List All Tracks", command=self.list_tracks_clicked).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.new_window, text="Enter Track Number").grid(row=0, column=1, padx=10, pady=10)

        
        
        # Input Fields
        self.input_track_txt = tk.Entry(self.new_window, width=5)
        self.input_track_txt.grid(row=0, column=2, padx=10, pady=10)

        # Buttons and Input Areas

        # Control Buttons
        tk.Button(self.new_window, text="Back to main menu", command=self.close_window).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.new_window, text="Add to list", command=self.add_tracks_clicked).grid(row=0, column=3, padx=10, pady=10)
        tk.Button(self.new_window, text="Clear list", command=self.clear_play_list).grid(row=0, column=4, padx=10, pady=10)
        tk.Label(self.new_window, text="Show the tracks with play count").grid(row=4, column=4, padx=10)
        tk.Button(self.new_window, text="Play track", command=self.play_track).grid(row=3, column=4, padx=10, pady=10)

        # ScrolledText Areas
        self.list_txt = tkst.ScrolledText(self.new_window, width=48, height=24, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=2, sticky="W", padx=10, pady=10)
        
        self.track_txt = tk.Text(self.new_window, width=45, height=24, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=(50,0), pady=10)

        self.play_count_txt = tk.Text(self.new_window, width=38, height=24) 
        self.play_count_txt.grid(row=1, column=4, padx=15)
        
        self.status_lbl = tk.Label(self.new_window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, sticky="W", padx=10, pady=10)
        
        tk.Label(self.new_window, text="Enter name for new track list").grid(row=2, column=1, padx=10, pady=10)
        self.list_name_entry = tk.Entry(self.new_window, width=20)
        self.list_name_entry.grid(row=2, column=2, padx=10, pady=10)

        tk.Button(self.new_window, text="Create Track List", command=self.create_track_list).grid(row=3, column=1, padx=(0,0))
        tk.Button(self.new_window, text="Show Track Lists", command=self.show_track_lists).grid(row=4, column=1, padx=(0,0))

        # ScrolledText Area to display track lists
        self.track_lists_display = tkst.ScrolledText(self.new_window, width=60, height=10)
        self.track_lists_display.grid(row=3, column=0, columnspan=5, padx=10, pady=10, rowspan=2)
    
    def create_track_list(self):
        #add new playlist with the selected track
        list_name = self.list_name_entry.get().strip()
        if not list_name:
            messagebox.showerror("Input Error", "Please enter a name for the track list.")
            return
        
        if list_name in self.track_lists:
            messagebox.showerror("Error", "A track list with this name already exists.")
            return

        self.track_lists[list_name] = self.selected_tracks.copy()  # save selected tracks

        messagebox.showinfo("Success", f"Track list '{list_name}' created successfully!")

    def show_track_lists(self):
        if not self.track_lists:
            set_text(self.track_lists_display, "No track lists created yet.")
            return

        display_text = "Track Lists:\n"
        for name, tracks in self.track_lists.items(): 
            display_text += f"{name}: {', '.join(str(track[0]) for track in tracks)}\n"

        set_text(self.track_lists_display, display_text)    
    
    def close_window(self):
        #Close the current window and show the main window
        self.new_window.destroy()
        self.window.deiconify()

        # mai fix - chưa xong 
    def play_track(self):
        if self.selected_tracks == []: #check if the list selectec_tracks equal [] 
            return messagebox.showerror("Error", "There is no track to play!")
        #Play the selected tracks          
        self.text_for_show = ""
        for key, track in self.selected_tracks:
            track.increment_play_count() # increase play count by 1           
            show_count = f"ID:{key} {track.get_name()} play count :{track.get_play_count()}\n"
            self.text_for_show += show_count
            
        set_text(self.play_count_txt, self.text_for_show)
        self.status_lbl.config(text="All selected tracks have been increased by 1!")
        self.open_youtube_link()

    def add_tracks_clicked(self):
       #Add track to the selected tracks list
        input_id = self.input_track_txt.get().replace(" ", "")  #recently updated this one to remove spaces
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

    def clear_play_list(self):
        #Clear the selected tracks list
        if self.selected_tracks == []:
            messagebox.showerror("Error", "There is nothing to clear!")
            self.status_lbl.config(text="Clear List button was clicked!")
            return        
        if not self.selected_tracks:
            return
        self.text_for_show = ""
        self.selected_tracks = []
        set_text(self.track_txt, self.text_for_show)
        self.status_lbl.config(text="Play list was cleared!")

    def open_youtube_link(self):
    # Check if the current index is within the range of selected tracks
        if self.index < len(self.selected_tracks):
            # Get the current track and its duration
            current_track = self.selected_tracks[self.index][1]  # `[1]` assumes `(key, track)` structure
            video_url = current_track.youtube_link
            duration = current_track.duration

            # Open the YouTube link in a web browser
            webbrowser.open(video_url)

            # Move to the next track after the duration of the current track
            self.index += 1
            self.window.after(duration * 1000, self.open_youtube_link)
        else:
            # Reset the index once all tracks are played
            self.index = 0
            self.status_lbl.config(text="All tracks in the list have been played.")

    def next_track(self):
        # Move to the next track
        self.index += 1
        # Call open_youtube_link only if there are more tracks to play
        if self.index < len(self.selected_tracks):
            self.open_youtube_link()
        else:
            print("Playlist finished.")  # All tracks have been played
            self.index = 0  # Reset index if needed





# ---------------------------------------- Draft Area------------------------------------------------------#
        # for track_key, selected_track in lib.library.items():
        #     self.selected_tracks.append((track_key, selected_track))

    # def open_youtube_link(self):
    #     if not self.is_playing and self.index < len(self.selected_tracks):
    #         self.is_playing = True
    #         tuple_track = self.selected_tracks[self.index]
    #         key, current_track = tuple_track
            
    #         video_url = current_track.youtube_link
    #         webbrowser.open(video_url)
    #         self.new_window.after(263 * 1000, self.next_track())
    #     else:
    #         print("All tracks have been played")
    # def open_youtube_link(self):
    # # Assuming `index` tracks the current position in `selected_tracks`
    #     if self.index < len(self.selected_tracks):
    #         current_track = self.selected_tracks[self.index]
            
    #         # Open the YouTube link of the current track
    #         webbrowser.open(current_track[1].youtube_link)  # Track details should have `youtube_link`
            
    #         # Schedule the next track after its duration
    #         self.window.after(current_track[1].duration * 1000, self.next_track)
    #         self.index += 1
    #     else:
    #         print("Finished playing all selected tracks.")
    #         self.index = 0