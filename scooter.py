class scooter():
    def __init__(self, battery , milleage , is_locked=True):
        self.battery = battery
        self.milleage = milleage
        self.is_locked = is_locked
        
        
    def start_ride(self):
        if self.battery > 25:
            self.is_locked = False
            self.battery = self.battery - 1
            self.milleage = self.milleage + 1
            return "RIDE_ACTIVE"
        else:
            return "LOW_BATTERY"
        
    
    def charge(self):
        self.battery = 100
        