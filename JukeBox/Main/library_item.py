class LibraryItem:          #here to pour value in
    def __init__(self, name, artist, rating, youtube_link, duration):
        self.name = name
        self.artist = artist
        self.rating = rating
        self._play_count = 0
        self.youtube_link = youtube_link
        self.duration = duration

    def info(self):         #a method() to return the info of an object
        return f"| {self.name} | {self.artist} | {self.stars()} |"
    
    def stars(self):    #this method will receive self.rating to create * and then return string of "*" to function
        stars = ""
        for i in range(self.rating):
            stars += "✰"
        return stars
    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_rating(self):
        return '*' * self.rating
    
    def get_play_count(self):
        return self._play_count
    
    def increment_play_count(self):
        self._play_count += 1
  
  