class Car:
    c_mileage_units = "Mi"
    #This __max_speed class  private variable with default value 
    __max_speed = 200

    @classmethod
    def print_units(cls):
        print(f"Mileage unit are {cls.c_mileage_units}")

    @staticmethod
    def static_hello():
        print(f"Hello I am a static method , I have not access to slef or cls objects.")

    #init funtion is constructor method in class
    def __init__(self,color,miles,model,eng_size):
        self.i_color = color
        self.i_mileage = miles
        #__no_doors is an example to private instance variable with default value in constructor method
        self.__no_doors = 4
        #_model is an example to protected instance variable ,added for illustration for only
        self._model =  model
        self.i_engine = self.Engine(eng_size) 

    #this __str__ help print statement implementation without any to_string() method
    def __str__(self):
        return f"{self.static_hello()} . {self.print_units()}. Car with color {self.i_color}, mileage {self.i_mileage}, model {self._model} and door {self.__doors()}. Car engine size is {car.i_engine.i_size}"
        
    #This doors method is private instance method in Car class
    def __doors(self):
        return self.__no_doors
    

    #That Engine class is an example to  Netsed  class
    class Engine:

        def __init__(self, size):
            self.i_size = size


if __name__ == "__main__":
    car = Car ("blue",1000,"Gentra","4x4")
    print(car)