import input_functions

# Task 6.1 T - use the code from 5.1 to help with this

class Track:
    def __init__(self, name, location):
        self.name = name
        self.location = location

# Reads in and returns a single track from the given file
def read_track(music_file):
    name = music_file.readline().strip()    #strip() is a string method that removes any leading and trailing whitespace from the string.
    location = music_file.readline().strip()
    track = Track(name, location)
    return track
    # Replace with your code

# Returns an array of tracks read from the given file
def read_tracks(music_file):
    count = int(music_file.readline())
    tracks = [] # create an empty list to hold the tracks
    index = 0
    while index < count:
        track = read_track(music_file)
        tracks.append(track)
        index = index + 1
    # Put a while loop here which increments an index to read the tracks
    return tracks

def print_tracks(tracks):
    x = 0
    while x < len(tracks):
        print(tracks[x].name)
        print(tracks[x].location)
        x = x + 1
    # print all the tracks use tracks[x] to access each track
    # Replace with your code

def print_track(track):
    print(f"Track title is: {track.title}")
    print(f"Track file location is: {track.file_location}")

# search for track by name
# returns the index of the track or -1 if not found
def search_for_track_name(tracks, search_string):    
    index = 0
    while index < len(tracks):
        if tracks[index].name.strip().lower() == search_string.strip().lower():
            return index
        index = index + 1
    return -1
    # put a while loop here that searches through the tracks
    # Use the read_string() function from input_functions.py to get the search string
    # NB: you might need to use .strip() to compare the strings correctly
    # put your code here.

def main():
    # Open the file using "with" to ensure it gets closed later
    with open("album.txt", "r") as music_file:
        tracks = read_tracks(music_file)
        print_tracks(tracks)

    search_string = input_functions.read_string("Enter the track name you wish to find: ")
    index = search_for_track_name(tracks, search_string)
    if index > -1:
        print(f"Found {tracks[index].name} at index {index}")
    else:
        print("Entry not found")
main()