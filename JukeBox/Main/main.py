from track_player import MainWindow
from tkinter import Tk 
import tkinter as tk
import font_manager as fonts

window = tk.Tk()
main_window = MainWindow(window)
fonts.configure() 
window.mainloop()