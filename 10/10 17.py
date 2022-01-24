import random
class Temp():
    def __init__(self):
        self_is_on=False
        self.temparature=36.6
    def on(self):
        self_is_on=True
        print("jest")
    def off(self):
        self_is_on=False
        print("nie jest")
    def mes(self):
        self.temparature=round(random.uniform(34.0,42.0),1)
        
    def display(self):
        if self.temparature>=37.0:
            print(f"Zmierzona temperatura {self.temparature}C (gorączka)")    
        else:
            print(f"Zmierzona temperatura {self.temparature}C")    
        if self.temparature>=41.0:
            print("Stan zagrożenia życia!!!") 
    
termometr=Temp()
termometr.on()
termometr.mes()
termometr.display()
termometr.off()