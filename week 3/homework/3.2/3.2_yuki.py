import input_functions as input_functions

# put your code below

class Track:
    # TODO: define the Track class with name and location attributes
    def __init__(self, track_name:str, track_location:str):
        self.name = track_name
        self.location = track_location


def read_track():
    print("Enter track")
    # TODO: prompt for and read the track name
    # TODO: prompt for and read the track location
    # TODO: create and return a Track object
    track_name = input_functions.read_string("Enter track name: ")
    track_location = input_functions.read_string("Enter track location: ")
    track = Track (track_name,track_location)
    return track
    


def print_track(track):
    # TODO: print the track name
    # TODO: print the track location
    print (f"Track name: {track.name}\nTrack location: {track.location}")


def main():
    # TODO: call read_track() and print_track()
    track = read_track()
    print_track(track)


# leave this line
if __name__ == "__main__":
    main()
