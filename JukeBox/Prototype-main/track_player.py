import tkinter as tk

import font_manager as fonts
from view_track import TrackViewer
from CreateTrackList import CreateTrackList
from UpdateTrack import UpdateTrack

class MainWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("JukeBox")
        self.window.geometry("520x250")
        self.window.configure(bg="gray")
        header_lbl = tk.Label(window, text="Juke Box")
        header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        view_tracks_btn = tk.Button(window, text="View Tracks", command=self.view_tracks_clicked)
        view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

        create_track_list_btn = tk.Button(window, text="Create Track List", command=self.view_create_track_clicked)
        create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)   #here is the button to create track list but without the command

        update_tracks_btn = tk.Button(window, text="Update Tracks", command=self.view_update_track_clicked)     #here is the button to update tracks but no command
        update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

        exit_btn = tk.Button(window, text="Exit", command=self.close_window)
        exit_btn.grid(row=2, column=0, padx=10, pady=10)

        status_lbl = tk.Label(window, bg='gray', text="", font=("Helvetica", 10))  #this one will appear when we clicked button
        status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)
        
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
        
        
window = tk.Tk()
main_window = MainWindow(window)
fonts.configure() 
window.mainloop()
