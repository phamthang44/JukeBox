import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as tkst
from tkinter import *
import track_library as lib
import font_manager as fonts
from Validation import InputValidation
from track_library import library_list
from library_item import LibraryItem
    
def set_text(text_area, content):           # inserts content into the text_area
    text_area.delete("1.0", tk.END)         #from 1.0 to end ?
    text_area.insert(1.0, content)          # then the new content is inserted

def add_text(text_area, content):
    text_area.insert(1.0, content)
     
class UpdateTracks(LibraryItem):
    def __init__(self, window):
        
        window.geometry("1150x550")
        window.title("Update Tracks")
        
        self.selected_tracks = []
        
        self.text_for_show = ""
        
        #button to show all tracks
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)
        
        
        #list area to show on left 
        self.list_txt = tkst.ScrolledText(window, width=48, height=48, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=2, sticky="W", padx=10, pady=10)

        #button to update track 
        update_track_btn = tk.Button(window, text="Update Track")
        update_track_btn.grid(row=0, column=3, padx=10, pady=10)
    
        self.update_track_txt = tkst.ScrolledText(window, width=48, height=48, wrap="none")
        self.update_track_txt.grid(row = 1, column = 3, columnspan=2, sticky="W", padx = 10, pady = 10)
    def update_tracks(self):
        pass
    
    


    def list_tracks_clicked(self):      #this function will appear the status of list tracks    
        track_list = lib.list_all()     
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")
if __name__ == "__main__":
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    UpdateTracks(window)     # open the TrackViewer GUI
    window.mainloop()  
    
    # run the window main loop, reacting to button presses, etc