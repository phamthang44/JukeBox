import csv
import io
import sys
from library_item import LibraryItem
#ensure the output use encode UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

library = {}

with open('D:\Desktop\GCS230575 - Python OOP\Coursework-main\JukeBox\Prototype-main\data.csv', mode="r", encoding='utf-8') as file:
    reader = csv.reader(file)
    
    for row in reader:
        if len(row) < 3:  # Đảm bảo có đủ dữ liệu
                    print("Row has insufficient data:", row)
                    continue
        track_id = row[0]
        track_name = row[1]
        artist = row[2]
        rating = int(row[3]) if len(row) > 3 else 0
        library[track_id] = LibraryItem(track_name, artist, rating)

#test for print 
# for key, item in library.items():
#     print(f"{key}: {item.info()}")


def search_string_key_number(key_number): #this function will take the parameter and check if in library then return string
    for key in library.keys(): 
        if int(key) == key_number:
            return key  #return a string key '01'
    return None
    
def get_key_number(key_string):  #this function also use for search
    if key_string in library:
        return int(key_string)  # Convert the key string to an integer
    else:
        raise ValueError(f"Key {key_string} does not exist in the library")
    # return int(library.keys)

def search_Item(key_number):
    for key, item in library.items():
        if int(key) == key_number:
            return item #return the object
    return None


def search_Item_by_key(key_number):
    for key, item in library.items():
        if int(key) == key_number:
            return key, item #if found will return the object in # Return the string key and the LibraryItem object
    return None, None #return None if go over the loop and not found!
       
def search_item_by_key(int_key): 
    for key, item in library.items():
        if int(key) == int_key:
            return item
    return None

def list_all() -> str:         #this function will list all of the object in library
    result = []
    for key, item in library.items():
        result.append(f"{key} {item.info()}")
    return "\n".join(result) 
    # 01 - info..... of Object


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_artist(key):    #it will receive Any -> return Any or None
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None  


def get_rating(key):    #this one will receive key from dictionary and return rating 
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1 


def set_rating(key, rating):    #This function will change the rating by receiving the key and rating to change because of the key map with the object
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


# def get_play_count(key):       #by receiving key to identify object with key and then return play_count number 
#     try:
#         item = library[key]
#         return item.play_count
#     except KeyError:
#         return -1



#----------- The old one ---------------


    

    

    

    

    
    
    
    
    
    
    
    
    