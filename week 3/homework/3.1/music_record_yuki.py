import input_functions as input_functions

GENRE_NAMES = { # Dictionary to store genre names
    1: "Pop",
    2: "Classic",
    3: "Jazz",
    4: "Rock"
}


class Album:
    # Optional: you may add an __init__ method
    def __init__(self, album_name:str, artist_name:str, Genre_number:int):
        self.name = album_name
        self.artist = artist_name
        self.genre = Genre_number

def read_album():
    print("Enter Album")

    # TODO: Read the album name (string)
    album_name = input_functions.read_string("")

    # TODO: Read the artist name (string)
    artist_name = input_functions.read_string("")

    # TODO: Read the genre number (integer between 1 and 4)
    Genre_number = input_functions.read_integer_in_range("")

    album = Album(album_name, artist_name, Genre_number)

    # TODO: Assign values to the album object
    # album.name =
    # album.artist =
    # album.genre =
    return album


def print_album(album):
    print(f"Album information is:\n {album.name} \n {album.artist}\n Genre is {album.genre}\n {GENRE_NAMES[album.genre]}")

    # TODO: Print album name
    # TODO: Print artist name
    # TODO: Print genre number
    # TODO: Print genre name using GENRE_NAMES dictionary


def main():
    album = read_album()
    print_album(album)


if __name__ == "__main__":
    main()
