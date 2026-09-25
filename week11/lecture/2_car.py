import input_functions as input_function


class CarData:
    def __init__(self):
        self.color = ""
        self.model = ""
        self.year = 0


def read_car():
    car = CarData()
    car.color = input_function.read_string("Enter car colour: ")
    car.model = input_function.read_string("Enter car model: ")
    car.year = input_function.read_integer("Enter car year: ")
    return car


def print_car(car):
    print(f"Car Colour: {car.color}")
    print(f"Car Model:  {car.model}")
    print(f"Car Year:   {car.year}")


def print_car_array(data, size):
    for i in range(size):
        print_car(data[i])


def populate_car_array(data, size):
    for i in range(size):
        # data.append(read_car())
        data[i] = read_car()


def main():
    CAR_SIZE = 3
    # cars = []
    cars = [CarData() for _ in range(CAR_SIZE)]
    populate_car_array(cars, CAR_SIZE)
    print_car_array(cars, CAR_SIZE)


main()
