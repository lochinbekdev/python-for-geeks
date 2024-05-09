class Car:
    c_mileage_units = "Mi"
    #This __max_speed class instance private 
    __max_speed = 200

    #init funtion is constructor function in class
    def __init__(self,color,miles,model,eng_size):
        self.i_color = color
        self.i_mileage = miles
        #__no_doors is an example to private attribute instance in class
        self.__no_doors = 4
        self._model =  model
        self.i_engine = self.Engine(eng_size) 

    def __str__(self):
        return f"car with color {self.i_color}, mileage {self.i_mileage}, model {self._model} and door {self.__doors()}. Car engine size is {car.i_engine.i_size}"
        
    #This doors method is private method in Car class
    def __doors(self):
        return self.__no_doors
    

    #That Engine class is an example to  Netsed  class
    class Engine:

        def __init__(self, size):
            self.i_size = size


if __name__ == "__main__":
    car = Car ("blue",1000,"Gentra","4x4")
    print(car)