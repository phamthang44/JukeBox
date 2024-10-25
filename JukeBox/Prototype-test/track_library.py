from library_item import LibraryItem


library = {'01': LibraryItem("Another Brick in the Wall", "Pink Floyd", 4),
           '02': LibraryItem("Stayin' Alive", "Bee Gees", 5), "03": LibraryItem("Highway to Hell ", "AC/DC", 2),
           '04': LibraryItem("Shape of You", "Ed Sheeran", 1), "05": LibraryItem("Someone Like You", "Adele", 3)}

# key - object is saved to dict - library
#key refers to the dictionary key (e.g., '01', '02', etc.).

#value refers to the corresponding value associated with that key in the dictionary. In this case, the value is an instance of the LibraryItem class.

# Create a list to store (key, value) tuples
library_list = []

#library_list[1] ~ tuple(key, value)

# Populate the list from the dictionary
for key, value in library.items():
    int_key = int(key)  # Convert the string key to an integer
    library_list.append((int_key, value))  # Append a tuple (int_key, value)
    #list = [(key, value), (key, value)]

def get_Item_by_key(int_key):
    for key, item in library_list:
        if key == int_key:
            return item #if found will return the object in
    return None #return None if go over the loop and not found!
        

def list_all() -> str:         #this function will list all of the object in library
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output
    # 01 - info..... of Object


def get_name(int_key):
    for key, item in library_list:
        if key == int_key:
            return item.name
    return f"Not Found!"    


def get_artist(int_key):    #it will receive Any -> return Any or None
    for key, item in library_list:
        if key == int_key:
            return item.artist
    return f"Not Found!"   


def get_rating(int_key):    #this one will receive key from dictionary and return rating 
    for key, item in library_list:
        if key == int_key:
            return item.rating
    return f"Not Found!"   


def set_rating(key, rating):    #This function will change the rating by receiving the key and rating to change because of the key map with the object
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(int_key):       #by receiving key to identify object with key and then return play_count number 
    for key, item in library_list:
        if key == int_key:
            return item.play_count
    return -1   



def increment_play_count(int_key):  # also like the function above but will increase by 1 when calling a function play music()
    for key, item in library_list:
        if key == int_key:
            item.play_count +=1
  

#----------- The old one ---------------

    # try:
    #     item = library[key]
    #     return item.play_count
    # except KeyError:
    #     return -1
    
    
    # try:
    #     item = library[key]
    #     item.play_count += 1
    # except KeyError:
    #     return
    
    # try:
    #     item = library[key]
    #     return item.rating
    # except KeyError:
    #     return -1
    
    # try:
    #     item = library[key]
    #     return item.name
    # except KeyError:
    #     return None
    
    # try:
    #     item = library[key]
    #     return item.artist
    # except KeyError:
    #     return None
    
    
    
    
    
    
    
    
    