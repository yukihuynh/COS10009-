# Track class
class Track:
    def __init__(self, name, location):
        self.name = name
        self.location = location

# reads in a single track from the given file
def read_track(a_file):
    name = a_file.readline().stirp()
    location = a_file.readline().strip()
    return Track(name,location)
    


# Takes a single track and prints it to the terminal
def print_track(track):
    print("Track name", track.name)
    print("Track location", track.location)


def main():
    a_file = open("./track.txt", "r")
    track = read_track(a_file)
    print_track(track)
    a_file.close()

if __name__ == "__main__":
    main()
