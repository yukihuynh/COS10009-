import input_functions
class Bird: 
     def __init__(self, bird_id:int, location:str, species:str, cage_number:int):
          self.id = bird_id
          self.location = location
          self.species = species
          self.cage_number = cage_number

def read_a_bird():
    bird_id = input_functions.read_integer("Enter bird id: ")
    location = input_functions.read_string("Enter bird location: ")
    species = input_functions.read_string("Enter bird species: ")
    cage_number = input_functions.read_integer("Enter bird cage number: ")

    bird = Bird(bird_id, location, species, cage_number)
    return bird

def read_birds():
    birds = [] # arrayy of birds
    count = input_functions.read_integer("How many birds are you entering: ") # get input for numbers of array
    i = 0
    while i < count:
         bird = read_a_bird()
         birds.append(bird) #adding inputs to array
         i += 1
    return birds

def print_a_bird(bird): #printing the inputs from the array
    print("Id", bird.id)
    print("Location", bird.location)
    print("Species", bird.species)
    print("Cage Number", bird.cage_number)

def print_birds(birds):
    i = 0
    while i < len(birds):   # tạo cái loop để in các thứ đã input vào
        print_a_bird(birds[i])
        i = i + 1

def main():
	birds = read_birds()
	print_birds(birds)

main()