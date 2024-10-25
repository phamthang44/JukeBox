import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as tkst
from tkinter import *
import track_library as lib
import font_manager as fonts
from Validation import InputValidation
from track_library import library_list, increment_play_count
from library_item import LibraryItem



def set_text(text_area, content):           # inserts content into the text_area
    text_area.delete("1.0", tk.END)         #from 1.0 to end ?
    text_area.insert(1.0, content)          # then the new content is inserted

def convert_input_number(input):
        try:
            track_number = int(input) #convert to integer

        except ValueError:
            messagebox.showerror("Input error", "Please enter a valid input number!.")
        if track_number < 0 or track_number > len(library_list):
            messagebox.showerror("Selection Error!", f"Please select a number between 1 and {len(library_list)}")
            return
        return track_number
     
class CreateTrackList():
    def __init__(self, window):     #constructor will get the self, and window
        self.new_window = tk.Toplevel(window)
        self.new_window.title("Create Track List")
        self.new_window.geometry("1300x720")    #will appear the window with width : 1150 and height : 550
           #this will appear in the title of the window
        #create a list with a void
        
        # Create a list to store selected tracks
        self.selected_tracks = []
        self.text_for_show = ""
        
        list_tracks_btn = tk.Button(self.new_window, text="List All Tracks", command=self.list_tracks_clicked)   #create button List All Tracks
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(self.new_window, text="Enter Track Number")    #the name beside the box to enter track number
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        #input_txt to make the area to input here 
        self.input_track_txt = tk.Entry(self.new_window, width=5)              #the box to entry
        self.input_track_txt.grid(row=0, column=2, padx=10, pady=10)

        #entry area to search
        self.input_toSearch_txt = tk.Entry(self.new_window, width=5)              #the box to entry
        self.input_toSearch_txt.grid(row=2, column=2, padx=10, pady=10)  
        #search button
        search_btn = tk.Button(self.new_window, text="Search ID ", command=self.search_func)
        search_btn.grid(row=3, column=2, padx=10, pady=10)
        #label 
        search_lbl = tk.Label(self.new_window, text="Enter Track Number")    #the name beside the box to enter track number
        search_lbl.grid(row=2, column=1, padx=10, pady=10)
        #appear the area to find search
        self.search_ID_txt = tk.Text(self.new_window, width=48, height=5, wrap="none")
        self.search_ID_txt.grid(row=3, column=3, sticky="W", padx=10, pady=10)
        
        #back to main menu
        back_btn = tk.Button(self.new_window, text="Back to main menu", command=self.close_window)
        back_btn.grid(row=2, column=0, padx=10, pady=10)
        
        add_track_btn = tk.Button(self.new_window, text="Add to list", command=self.add_tracks_clicked)        
        #this btn will add track to list
        add_track_btn.grid(row=0, column=3, padx=10, pady=10)                                         #then when calling successfully it will return the info of Object inside

        #clear button
        clear_btn = tk.Button(self.new_window, text="Clear list", command=self.clear_play_list)
        clear_btn.grid(row=0, column=4, padx=10, pady=10)
        
        #play button I think this is for fun !
        play_btn = tk.Button(self.new_window, text="Play track", command=self.play_track)
        play_btn.grid(row=1, column=4, padx=10, pady=10)
        
        #Area to appear the list on left
        self.list_txt = tkst.ScrolledText(self.new_window, width=48, height=24, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=2, sticky="W", padx=10, pady=10)
        
        #this area will show the new track list when add to list btn was pressed
        
        self.track_txt = tk.Text(self.new_window, width=48, height=24, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)
        self.status_lbl = tk.Label(self.new_window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, sticky="W", padx=10, pady=10)
        self.window = window
        
    def close_window(self):
        self.new_window.destroy()  # Close the second window
        self.window.deiconify()
        
    #play_btn function to show status
    def play_track(self):
        input = self.input_track_txt.get()
        track_number = convert_input_number(input)

        for track_key, track in self.selected_tracks:
            if track_number == track_key:
                increment_play_count(track_number)
                self.status_lbl.configure(text="Playing...")
                return
        
    def add_tracks_clicked(self):
        input = self.input_track_txt.get()
        track_number = convert_input_number(input)
        #this one will check if it has exception
        #it will show the message error base on situation 
        #this when success will show messagebox  
        #because in track_library I put the key and Object into a tuple 
        #so before call function info() I will unpack it    
        selected_tuple = library_list[track_number - 1] # Access by index
        
        int_key, selected_track = selected_tuple    #this one call unpacking
        
        #loop to check if int_key == track_key will print Error because iterate
        for track_key, track in self.selected_tracks:
            if track_key == int_key:
                messagebox.showerror("Fail (Duplicate)", f"The track {track_key} is already in the list!")
                return

        self.selected_tracks.append((int_key, selected_track))  
        #track_details = f"{key} {name} - {artist} - {rating}\n"
        messagebox.showinfo("Success", f"Track '{track_number}' added to your selected tracks.")
        self.status_lbl.configure(text="Track was added to play list!")
        track_details = f"{track_number} - {selected_track.info()}\n"
        self.text_for_show = self.text_for_show + track_details
        #this will print to entry area

        set_text(self.track_txt, self.text_for_show)
        self.status_lbl.configure(text="Track was added to play list!")
        return track_number

    # this function will show the Tracks  

    def list_tracks_clicked(self):      #this function will appear the status of list tracks    
        track_list = lib.list_all()     
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")
        
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

    #sort 
    # def sort_id_descending(self):   
    #     self.selected_tracks.sort()
    #     return  
    
    #clear list function 
    def clear_play_list(self):
        if(not len(self.selected_tracks)):
            return
        self.text_for_show = ""
        self.selected_tracks = []
        #for loop to read all the list and reset
        set_text(self.track_txt , self.text_for_show)
        self.status_lbl.configure(text="Play list was cleared!")

#-------------------- Draft Area-----------------------------#
    
# if __name__ == "__main__":
#     window = tk.Tk()        # create a TK object
#     fonts.configure()       # configure the fonts
#     CreateTrackList(window)     # open the TrackViewer GUI
#     window.mainloop()       # run the window main loop, reacting to button presses, etc


        # self.list_tracks_clicked()
        #need to create a new button to put all the things you just add to list
        #into a new List[] to store as a new object ?
        
        
    #search the name, id, artist
    #def search_by_ID(self):
        # text_for_show = ""
        # input = self.input_toSearch_txt.get()
        # keyword = convert_input_number(input)
        # selected_tuple = library_list[keyword - 1] # Access by index
        
        # int_key, selected_track = selected_tuple    #this one call unpacking
        
        # #loop to check if int_key == track_key will print Error because iterate
        # for track_key, track in self.selected_tracks:
        #     self.selected_tracks.append((int_key, selected_track)) 
        #     if track_key == keyword:
        #         track_details = f"{keyword} - {selected_track.info()}\n"
                
        # set_text(text_for_show, track_details)  
        
        
        
    #def showDetails(self):    
    
    
    
    #------------------------------------------------------------
    # def view_tracks_clicked(self):
    #     key = self.input_txt.get()      #must be like the key in the object in file library_item if it's not similar to that it will return else
    #     name = lib.get_name(key)
    #     if name is not None:
    #         artist = lib.get_artist(key)
    #         rating = lib.get_rating(key)
    #         play_count = lib.get_play_count(key)
    #         track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
    #         set_text(self.track_txt, track_details)
    #     else:
    #         set_text(self.track_txt, f"Track {key} not found")
    #     self.status_lbl.configure(text="View Track button was clicked!") #finally it will appear the status
    #------------------------------------------------------------
        # if not in (1..5) will say "Please select a number between 1 and 5"
        # if in (1..5) but input string or sth instead of number
        # it will say "Please enter a valid input number!."
        # try:
        #     track_number = int(input_number) #convert to integer
        #     return track_number
        # except ValueError:
        #     messagebox.showerror("Input error", "Please enter a valid input number!.")
        # if track_number < 0 or track_number > len(library_list):
        #     messagebox.showerror("Selection Error!", f"Please select a number between 1 and {len(library_list)}")
        #     return