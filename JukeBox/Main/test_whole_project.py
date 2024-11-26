from library_item import LibraryItem

def test_add_track():
    tracks = []
    
    song = LibraryItem("Test","test",5,"https://www.youtube.com/watch?v=JgTZvDbaTtg&list=RDJgTZvDbaTtg&index=2",328)
    song2 = LibraryItem("Test2","test2",5,"https://www.youtube.com/watch?v=JgTZvDbaTtg&list=RDJgTZvDbaTtg&index=2",328)
    tracks.append(song)
    tracks.append(song2)
    
    assert tracks[0].name == "Test"
    assert tracks[1].name == "Test2"

def test_empty_selected_tracks():
    selected_tracks = []
    assert len(selected_tracks) == 0

def test_duplicate_track_in_list():
    selected_tracks = []
    song = LibraryItem("Test","test",5,"https://www.youtube.com/watch?v=JgTZvDbaTtg&list=RDJgTZvDbaTtg&index=2",328)
    song2 = LibraryItem("Test","test2",5,"https://www.youtube.com/watch?v=JgTZvDbaTtg&list=RDJgTZvDbaTtg&index=2",328)
    selected_tracks.append(song)
    selected_tracks.append(song2)
    
    assert len(selected_tracks) == 2
    assert selected_tracks[0].name == selected_tracks[1].name

def convert_input_number(input_value):
    if input_value is None:
        return None
    try:
        # Convert to float first to handle decimal inputs like 1.1
        number = float(input_value)
        # Convert to integer for valid whole numbers
        return int(number)
    except (ValueError, TypeError):
        return None
   
def test_valid_number_input():
    # Inputs
    input1 = "10"
    input2 = "01"
    input3 = 1.1
    input4 = 2
    input5 = None
    input6 = 5
    
    # Assume convert_input_number is defined elsewhere
    valid_input_1 = convert_input_number(input1)
    valid_input_2 = convert_input_number(input2)
    valid_input_3 = convert_input_number(input3)
    valid_input_4 = convert_input_number(input4)
    valid_input_5 = convert_input_number(input5)
    valid_input_6 = convert_input_number(input6)
    
    # Assertions
    assert valid_input_1 == 10
    assert valid_input_2 == 1
    assert valid_input_3 == 1
    assert valid_input_4 == 2
    assert valid_input_5 is None
    assert valid_input_6 == 5
    
    
def test_valid_name_list():
    list_name = "Test list name"
    list_name2 = "  Test list name   "
    check_space = list_name2.strip()

    # Check the list name is not None
    assert list_name is not None

    # Ensure list_name matches the expected value
    assert list_name == "Test list name"

    # Ensure whitespace is removed correctly
    assert list_name2 == "  Test list name   "  # Original string with spaces
    assert check_space == "Test list name"      # Trimmed string
    
def test_remove_track():
    tracks = []
    
    song = LibraryItem("Test","test",5,"https://www.youtube.com/watch?v=JgTZvDbaTtg&list=RDJgTZvDbaTtg&index=2",328)
    song2 = LibraryItem("Test2","test2",5,"https://www.youtube.com/watch?v=JgTZvDbaTtg&list=RDJgTZvDbaTtg&index=2",328)
    tracks.append(song)
    tracks.append(song2)
    
    assert tracks is not None
    assert len(tracks) == 2

    tracks.remove(song)
    assert len(tracks) == 1
    
    tracks.remove(song2) 
    assert len(tracks) == 0
    assert tracks == []
    

test_duplicate_track_in_list()
test_empty_selected_tracks()
test_add_track()
test_valid_number_input()
test_valid_name_list()
test_remove_track()