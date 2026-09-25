import input_functions as input_function 
Genre_Names = {
    1:"Pop",
    2:"Classic",
    3:"Jazz", 
    4:"Rock" 
}
class Album(): 
    def __init__(self, album_name:str, artist_name:str, Genre_number:int):
        self.name = album_name
        self.artist = artist_name
        self.genre = Genre_number

def read_album():
    print ("Enter Album")
    album_name = input_function.read_string("Enter album name: ") 
    artist_name = input_function.read_string("Enter aritist name: ")
    Genre_number = input_function.read_integer_in_range("Enter genre between 1-4:")
    album = Album (album_name, artist_name, Genre_number)
    return album 

def print_album(album): 
    print (f"Album information is:\n {album.name}\n {album.artist}\n Genre is {album.genre}\n {Genre_Names[album.genre]}")

def main():
    album = read_album()
    print_album(album)

if __name__ == "__main__":
    main()
    