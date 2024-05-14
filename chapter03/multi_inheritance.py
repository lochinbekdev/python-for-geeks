class Vehicle:
    def __init__(self,color):
        self.i_color = color

    def print_vehicle_info(self):
        print(f"This is a vehicle an I know my color is {self.i_color}")

class Engine:
    def __init__(self,size):
        self.i_size = size


    def print_engine_info(self):
        print(f"This is Engine and I know my size is {self.i_size}")

class Car(Vehicle,Engine):

    def __init__(self, color,size,seats):
        self.i_color = color
        self.i_size = size
        self.i_seats = seats

    def print_car_info(self):
        print(f"Car with color {self.i_color} and no of seats {self.i_seats} with engine of size {self.i_size}") 


if __name__ == "__main__":
    car = Car("blue","4.8L",4)
    car.print_vehicle_info()
    car.print_engine_info()
    car.print_car_info()
