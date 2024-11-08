import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as tkst
from tkinter import *
from CreateTrackList import CreateTrackList
import track_library as lib
from track_library import search_Item
import font_manager as fonts


def set_text(text_area, content):           # inserts content into the text_area
    text_area.delete("1.0", tk.END)         # first the existing content is deleted
    text_area.insert(1.0, content)          # then the new content is inserted


class TrackViewer():
    def __init__(self, window):     #constructor will get the self, and window
        self.new_window = tk.Toplevel(window)
        self.new_window.geometry("750x350")    #will appear the window with width : 750 and height : 350
        self.new_window.title("View Tracks")   #this will appear in the title of the window

        
        list_tracks_btn = tk.Button(self.new_window, text="List All Tracks", command=self.list_tracks_clicked)   #create button List All Tracks
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(self.new_window, text="Enter Track Number")    #the name beside the box to enter track number
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(self.new_window, width=3)              #the box to entry
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_track_btn = tk.Button(self.new_window, text="View Track", command=self.view_tracks_clicked)        #this will call function view_tracks_clicked
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)                                         #then when calling successfully it will return the info of Object inside

        #back to main menu
        back_btn = tk.Button(self.new_window, text="Back to main menu", command=self.close_window)        #this will call function view_tracks_clicked
        back_btn.grid(row=1, column=3, padx=10, pady=10) 


        self.list_txt = tkst.ScrolledText(self.new_window, width=48, height=12, wrap="none") #this one will the area information of tracks 
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.track_txt = tk.Text(self.new_window, width=24, height=4, wrap="none") #this one will the area information of a track  
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(self.new_window, text="", font=("Helvetica", 10)) #this one will update the status when user press some buttons
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        
        self.list_tracks_clicked()
        self.new_window.protocol("WM_DELETE_WINDOW", self.close_window) #this one will help the program shutdown completely when press X on right of window or Exit buttons
        self.window = window
    
    def close_window(self):
        self.new_window.destroy()  # hide this current window
        self.window.deiconify() # this will back to main window of track player 
        
    def view_tracks_clicked(self):
        key = self.input_txt.get().replace(" ", "") #take the keyword in the area and remove spaces 

        checkKeyWord = convert_input_number(key) #convert to int 
        item = search_Item(checkKeyWord) #get object from library 
        
        if item is not None:
            name = item.name
            artist = item.artist
            stars = item.stars()
            play_count = item._play_count
            track_details = f"{name}\n{artist}\nrating: {stars}\nplays: {play_count}" #f"string to show the info of a track
            set_text(self.track_txt, track_details) #set text on the area to show info 
        else:
            return f"Not Found this track!" # if not found will return this f'string 
        self.status_lbl.configure(text="View Track button was clicked!") #finally it will appear the status

    def list_tracks_clicked(self):      #this function will appear the status of list tracks    
        track_list = lib.list_all()     #call list_all() function in track_library
        set_text(self.list_txt, track_list) 
        self.status_lbl.configure(text="List Tracks button was clicked!") #update the status label 


def convert_input_number(input): #function to convert 
        try:
            track_number = int(input) #convert to integer

        except ValueError:
            messagebox.showerror("Input error", "Please enter a valid input number!.")
        if track_number < 0 or track_number > len(lib.library):
            messagebox.showerror("Selection Error!", f"Please select a number between 1 and {len(lib.library)}")
            return
        return track_number
