class Car:

    def __init__(self, name = "General", model = "GM", car_type = "saloon"):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = 0

        if self.name == "Porsche" or self.name == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        
        if self.car_type == "saloon":
            self.num_of_wheels = 4
        else:
            self.num_of_wheels = 8
    
    def is_saloon(self):
        if self.car_type == "saloon":
            return True
        else:
            return False
    
    def drive(self, drive_mode):
        if drive_mode == 7:
            self.speed = 77
        elif drive_mode == 3:
            self.speed = 1000
        
        return self
    


