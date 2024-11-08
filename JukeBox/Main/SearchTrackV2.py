import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as tkst
import track_library as lib
from PIL import Image, ImageTk
#store the path of image 
track_images = {
    "01" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\1.jpg",
    "02" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\2.jpg",
    "03" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\3.jpg",
    "04" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\4.jpg",
    "05" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\5.jpg"
}

track_images_name = {
    "Another Brick in the Wall" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\1.jpg",
    "Stayin' Alive" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\2.jpg",
    "Highway to Hell" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\3.jpg",
    "Shape of You" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\4.jpg",
    "Someone Like You" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\5.jpg"
}

track_images_artist = {
    "Pink Floyd" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\1.jpg",
    "Bee Gees" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\2.jpg",
    "AC/DC" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\3.jpg",
    "Ed Sheeran" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\4.jpg",
    "Adele" : r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\5.jpg"
}

class SearchTrack:
    def __init__(self, window):
        self.window = window
        self.new_window = tk.Toplevel(window)
        self.new_window.title("Search Track")
        self.new_window.geometry("1150x600")

        # Tải ảnh và giữ tham chiếu
        # pil_image = Image.open(r"D:\Desktop\GCS230575 - Python OOP\Coursework-main\image\test.jpg")
        # self.image = ImageTk.PhotoImage(pil_image)  # Không cần size ở đây, nó không hợp lệ với PhotoImage
        
        self.list_image = []
        self.image = None #store the reference
        self.new_window.protocol("WM_DELETE_WINDOW", self.close_window)
        self.initGUI()

    def initGUI(self):
        # Placeholder for the entry
        self.entry = tk.Entry(self.new_window, foreground="gray", bg="gray")
        self.entry.insert(0, "Type your track name here...")
        self.entry.bind("<FocusIn>", self.on_entry_click)
        self.entry.bind("<FocusOut>", self.on_focus_out)
        self.entry.grid(row=1, column=0, padx=10, pady=10)
        self.entry.bind("<Return>", lambda event: self.search_song())

        # Place to show text 
        self.list_txt = tkst.ScrolledText(self.new_window, width=60, height=20, wrap="none", bg="gray")
        self.list_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text area to show description and image 
        self.text = tkst.ScrolledText(self.new_window, width=60, height=25, wrap="none", bg="gray")
        self.text.grid(row=2, column=3, sticky="W", padx=10, pady=10)

        back_btn = tk.Button(self.new_window, text="Back to main menu", command=self.close_window, bg="gray", fg="#6CEC44")
        back_btn.grid(row=3, column=0, padx=10, pady=10)

    def close_window(self):
        self.new_window.destroy()  # Đóng cửa sổ tìm kiếm
        self.window.deiconify()  # Hiển thị lại cửa sổ chính

    def on_entry_click(self, event):
        if self.entry.get() == "Type your track name here...":
            self.entry.delete(0, tk.END)
            self.entry.configure(foreground="black")

    def on_focus_out(self, event):
        if self.entry.get() == "":
            self.entry.insert(0, "Type your track name here...")
            self.entry.configure(foreground="gray")

                    

    #     # Display results in ScrolledText
    #     self.set_text(self.list_txt, text_for_show if text_for_show else "Not Found")
    def search_song(self):
        keyword = self.entry.get().replace(" ", "")
        text_for_show = ""

        self.text.delete(1.0, tk.END)  # Clear the previous text and images

        # Counter for limiting the number of tracks to show
        track_count = 0
        # Check if the keyword matches the name or ID of the track
        for song_id, song_info in lib.library.items():
            if keyword.lower() in song_id.lower() or keyword.lower() in song_info.name.lower() or keyword.lower() in song_info.artist.lower():
                text_for_show += f"{song_info.info()}\n"

                # Load the image for the current song
                image_path = track_images.get(song_id) or track_images_name.get(song_info.name) or track_images_artist.get(song_info.artist)
                if image_path:
                    image = self.load_image(image_path, size=(200, 200))  # Load the image
                    self.list_image.append(image)
                    if image and track_count < 5:
                        self.text.image_create(tk.END, image=image)  # Insert the image
                        self.image = image  # Keep a reference to prevent garbage collection
                        
                        track_count += 1
        if track_count == 0:
            self.text.insert(tk.END, "No matching tracks found.")                
        # Display results in ScrolledText
        self.set_text(self.list_txt, text_for_show if text_for_show else "Not Found")

        # Chèn ảnh vào text area
        # self.text.delete(1.0, tk.END)  # Xóa nội dung cũ
        # self.text.insert(tk.END, "Track Information\n")  # Thêm tiêu đề mô tả
        # self.text.image_create(tk.END, image=self.image)  # Chèn ảnh
        # self.text.insert(tk.END, "\nDescription goes here...")  # Thêm mô tả

    def set_text(self, widget, text):
        widget.delete(1.0, tk.END)
        widget.insert(tk.END, text)

    def load_image(self, image_path, size=None):
        try:
            pil_image = Image.open(image_path)
            
            if size:
                pil_image = pil_image.resize(size)  # Remove Image.ANTIALIAS
            
            photo_image = ImageTk.PhotoImage(pil_image)
            
            return photo_image
        
        except Exception as e:
            print(f"Error loading image: {e}")
            return None
        
        #============================================================
    # def search_song(self):
    #     keyword = self.entry.get()
    #     text_for_show = ""
        
    #     self.text.delete(1.0, tk.END)

    #     # test if keyword in name of track or track id 
    #     for song_id, song_info in lib.library.items():
    #         if keyword.lower() in song_id.lower() or keyword.lower() in song_info.name.lower():
    #             text_for_show += f"{song_info.info()}\n"
                
    #             if song_id in track_images:
    #                 image_path = track_images[song_id]
    #                 self.image = self.load_image(image_path, size=(200, 200))  # Store the reference
    #             elif song_info.name in track_images_name:
    #                 image_path = track_images_name[song_info.name]
    #                 self.image = self.load_image(image_path, size=(200, 200))  # Store the reference
    #             else:
    #                 self.image = None

    #             if self.image:
    #                 self.text.image_create(tk.END, image=self.image)  # Insert the image into the ScrolledText