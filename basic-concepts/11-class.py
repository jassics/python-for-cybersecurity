"""
Parent Class
"""
class Laptop:
    def __init__(self):
        # minimum specs
        self.cpu = "i3 10th Gen"
        self.gpu = "MX 130"
        self.ram = "8 GB"
        self.display = "1080p"
        self.battery = "60 WHr"
        self.storage = "256 GB SSD"
    

    def setSpecifications(self,specs:dict):
        try:
            self.model = specs["model"]
            self.cpu = specs["cpu"]
            self.gpu = specs["gpu"]
            self.ram = specs["ram"]
            self.display = specs["display"]
            self.battery = specs["battery"]
            self.storage = specs["storage"]

        except Exception as e:
            print("All attributes not passed in specs")
            exit()
            
    def getSpecifications(self):
        print(f"Model: {self.model}")
        print(f"CPU: {self.cpu}")
        print(f"GPU: {self.gpu}")
        print(f"RAM: {self.ram}")
        print(f"Display: {self.display}")
        print(f"Battery: {self.battery}")
        print(f"Storage: {self.storage}")




"""
Single-level Inheritance
(Child Class)
"""
class GamingLaptop(Laptop):
    def __init__(self,specs:dict):
        print("Gaming Laptop")
        #Set the passed specs
        super().setSpecifications(specs)

        # Gaming laptoip features (extra)
        self.refresh_rate = "144 Hz"
        self.response_time = "2ms"        

    def getGamingSpecs(self):
        super().getSpecifications()
        print(f"Refresh Rate: {self.refresh_rate}")
        print(f"Response Time: {self.response_time}")






if __name__ == "__main__":

    gaming_specs = {
        "cpu" : "i7 12th Gen",
        "gpu" : "RTX 3070 Ti",
        "ram" : "16 GB",
        "display" : "1440p",
        "battery" : "90 WHr",
        "storage" : "1 TB NVME M.2 SSD"
    }

    #         "model": "ASUS TUF Gaming A15",

    gl = GamingLaptop(specs=gaming_specs)
    gl.getGamingSpecs()