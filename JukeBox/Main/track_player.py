import tkinter as tk

import font_manager as fonts
from view_track import TrackViewer
from CreateTrackList import CreateTrackList
from UpdateTrack import UpdateTrack
from SearchTrackV2 import SearchTrack
class MainWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("JukeBox")
        self.window.geometry("520x200")
        self.window.configure(bg="#131313")
        
        self.initUI()
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)
    
    def initUI(self):
        header_lbl = tk.Label(self.window, text="Juke Box Music App", fg="#1db954")
        header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        header_lbl.configure(bg="#131313")

        view_tracks_btn = tk.Button(self.window, text="View Tracks", command=self.view_tracks_clicked, bd=0, fg="#1db954")
        view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)
        view_tracks_btn.configure(bg="#6b6b6b")
        create_track_list_btn = tk.Button(self.window, text="Create Track List", command=self.view_create_track_clicked, bd=0, fg="#1db954")
        create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)   #here is the button to create track list but without the command
        create_track_list_btn.configure(bg="#6b6b6b")

        update_tracks_btn = tk.Button(self.window, text="Update Tracks", command=self.view_update_track_clicked, bd=0, fg="#1db954")     #here is the button to update tracks but no command
        update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)
        update_tracks_btn.configure(bg="#6b6b6b")
        
        exit_btn = tk.Button(self.window, text="Exit", command=self.close_window, bd=0, fg="#1db954")
        exit_btn.grid(row=2, column=0, padx=10, pady=10)
        exit_btn.configure(bg="#6b6b6b")
        
        search_btn = tk.Button(self.window, text="Search", command=self.view_search_track, bd=0, fg="#1db954")
        search_btn.grid(row=2, column=1, padx=10, pady=10)
        search_btn.configure(bg="#6b6b6b")
    
    def view_tracks_clicked(self):
        self.window.withdraw() #configure take from font_manager will change the text into that font 
        TrackViewer(self.window)

    
    def view_create_track_clicked(self):
        self.window.withdraw()
        CreateTrackList(self.window)
    
    def close_window(self):
        exit()
    
    def view_update_track_clicked(self):
        self.window.withdraw()
        UpdateTrack(self.window)    
        
    def view_search_track(self):
        self.window.withdraw()
        SearchTrack(self.window)
        
        

