class Track:
    def __init__(self, name, location):
        self.name = name
        self.location = location

def read_tracks(music_file):
    count = int(music_file.readline().strip())
    tracks = []
    index = 0 
    while index < count:
        track = read_track(music_file)
        tracks.append(track)
        index = index + 1    
    # Put a while loop here which increments an index to read the track
    return tracks

def read_track(music_file):
    name = music_file.readline().strip()
    location = music_file.readline().strip()
    track = Track(name, location)
    return track

def print_tracks(tracks):
    index = 0
    while index < len(tracks):
        print_track(tracks[index])
        index = index + 1
    # Replace with code
    # Use a while loop with a control variable index
    # to print each track. Use tracks.length to determine how
    # many times to loop.

    # Print each track use: tracks[index] to get each track record

def print_track(track):
    print(f"Track Name: {track.name}")
    print(f"Track Location: {track.location}")

def main():
    music_file = open("input.txt", "r") # Open for reading
    
    #Print all the tracks
    tracks = read_tracks(music_file)
    print_tracks(tracks)
    music_file.close()
main()