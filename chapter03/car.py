class Car:

    c_mileage_units='Mi'

    def __init__(self,color,miles):
        self.i_color = color
        self.i_milesage = miles

if __name__ == "__main__":
    
    car1 = Car ('red',1000)
    print(car1.c_mileage_units)
    print(car1.i_milesage)