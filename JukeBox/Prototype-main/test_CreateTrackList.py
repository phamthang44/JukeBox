import pytest
from CreateTrackList import convert_input_number
from track_library import search_Item
import track_library

# Assuming `track_library` has a `library` dictionary of track objects
def display_library_data():
    for track_id, track in track_library.library.items():
        print(f"ID: {track_id}, Track Info: {track.info()}")  # Customize with your attributes



def test_convert_input_number():
    valid_input = "01"
    invalid_input = "abc"  # non-numeric

    # Test valid conversion
    assert convert_input_number(valid_input) == int(valid_input)

    # Test invalid input handling (should return None)
    assert convert_input_number(invalid_input) is None

def test_search_Item():
    valid_key_number = "01"
    invalid_key_number = "abc"
    invalid_key_number_2 = "999"
    
    assert search_Item(valid_key_number) is not None, "Valid key returned None!"
    assert search_Item(invalid_key_number) is None     
    assert search_Item(invalid_key_number_2) is None, "Invalid key did not return None!"

if __name__ == "__main__":
    pytest.main()
    display_library_data()
    test_convert_input_number()
    test_search_Item()
