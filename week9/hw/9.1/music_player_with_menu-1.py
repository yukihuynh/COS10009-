import input_functions 

GENRE = {
    1 : "Pop",
    2 : "Classic",
    3 : "Jazz",
    4 : "Rock"
}

# ----------------------------
# CLASSES---------------------
# ----------------------------
class Album: #tạo class Album
    def __init__(self, artist, name_album, release_date, genre, tracks):
        self.artist = artist
        self.name = name_album
        self.release = release_date
        self.genre = genre
        self.tracks = tracks


class Track():
    def __init__(self, name, location):
        self.name = name
        self.location = location


# ----------------------------
# READ FILE-------------------
# ----------------------------
#đọc các name,location từ class Track
def read_track(music_file): 
    name = music_file.readline().strip()
    location = music_file.readline().strip()
    return Track(name, location)

#tạo array, append name,location vào lưu lại 
def read_tracks(music_file): 
    count = int(music_file.readline()) 
    tracks = []
    index = 0 
    while index < count:
        track = read_track(music_file)
        tracks.append(track)
        index += 1
    return tracks

#đọc các thành phần trong Album class
def read_album(music_file):
    artist = music_file.readline().strip()
    name_album = music_file.readline().strip()
    release_date = music_file.readline().strip()
    genre = int(music_file.readline())
    tracks = read_tracks(music_file)
    return Album(artist, name_album, release_date, genre, tracks)

#tạo thêm 1 array ablums để append các data:
def read_albums(filename): 
    albums = [] 
    with open(filename, "r") as music_file:
        count = int(music_file.readline())
        i = 0 
        while i < count: 
            album = read_album(music_file)
            albums.append(album)
            i += 1
    return albums

# ----------------------------
# DISPLAY----------------------
# ----------------------------
def print_track(track): 
    print(f"Track: {track.name}")
    print(f"Location: {track.location}")

def print_tracks(tracks):
    i = 0 
    while i < len(tracks):
        print(f"{i+1}. {tracks[i].name}")   
        i += 1

def print_album(album, index):
    print(f"{index+1}. {album.name} by {album.artist} ({album.release}) - {GENRE[album.genre]}")

def display_albums(albums):
    if len(albums) == 0:
        print("No albums loaded.")
        return

    i = 0
    while i < len(albums):
        print_album(albums[i], i)
        i += 1


def display_by_genre(albums):
    print("\nAvailable genres:")
    i = 1
    while i <= len(GENRE):
        print(f"{i}. {GENRE[i]}")
        i += 1

    choice = input_functions.read_int("Select genre: ")

    i = 0
    while i < len(albums):
        if albums[i].genre == choice:
            album = albums[i]
            print(f"{i+1}. {album.name} by {album.artist} ({album.release}) - {GENRE[album.genre]}")
        i += 1

# ----------------------------
# PLAY-------------------------
# ----------------------------
def play_album(albums):
    if len(albums) == 0:
        print("No albums loaded.") 
        return

    index = input_functions.read_int("Enter album number: ") - 1  

    if index < 0 or index >= len(albums):
        print("Invalid album")
        return

    album = albums[index]

    print("\nTracks:")
    print_tracks(album.tracks)

    track_num = input_functions.read_int("Choose track: ") - 1  
    if track_num < 0 or track_num >= len(album.tracks):
        print("Invalid track")
        return

    track = album.tracks[track_num]

    print(f"\nPlaying track {track.name} from album {album.name}...")

# ----------------------------
# UPDATE ALBUM----------------
# ----------------------------
def update_album(albums):
    if len(albums) == 0:
        print("No albums loaded.")
        return

    print("\nAlbums:")
    display_albums(albums)

    index = input_functions.read_int("Enter album number to update: ") - 1  
    if index < 0 or index >= len(albums):
        print("Invalid album")
        return

    album = albums[index]

    print("\n1. Update Title")
    print("2. Update Genre")
    choice = input_functions.read_int("Select option: ")

    if choice == 1:
        new_title = input_functions.read_string("Enter new title: ")
        album.name = new_title

    elif choice == 2:
        print("\nAvailable genres:")
        i = 1
        while i <= len(GENRE):
            print(f"{i}. {GENRE[i]}")
            i += 1           
        new_genre = input_functions.read_int("Enter genre number: ")
        if new_genre in GENRE:
            album.genre = new_genre
        else:
            print("Invalid genre")
            return
    else:
        print("Invalid option")
        return

    print("\nUpdated album:")
    print_album(album, index)
    input("Press Enter to return to menu!!!")


# ----------------------------
# MAIN MENU----------------------
# ----------------------------
def menu():
    print("\nMusic Player")
    print("1. Read Albums")
    print("2. Display Albums")
    print("3. Select an Album to play")
    print("4. Update an existing Album")
    print("5. Exit")

# ----------------------------
# MAIN-------------------------
# ----------------------------
def main(): 
    albums = []
    finished = False

    while not finished: 
        menu()    
        choice = input_functions.read_int("Select option: ")
        match choice:
            case 1:
                filename = input_functions.read_string("Enter filename: ")
                albums = read_albums(filename)
                print("Albums loaded!")
            case 2: 
                sub = input_functions.read_int("1. All Albums  2. By Genre: ")
                match sub:
                    case 1: 
                        display_albums(albums)
                    case 2:
                        display_by_genre(albums)
                    case _:
                        print("Invalid option")
            case 3: 
                play_album(albums)
            case 4:
                update_album(albums)
            case 5:
                print("Goodbye!")
                finished = True
            case _: 
                print("Please enter a valid option")


main()