from scooter import scooter 

def test_scooter_ride():
        
    test_scooter = scooter(80, 10, True)
    
    result = test_scooter.start_ride()
    
    assert result == "RIDE_ACTIVE"
    
    assert test_scooter.is_locked == False
    
def test_scooter_low_battery():
    dead_scooter = scooter(0, 10 ,True)
    
    result = dead_scooter.start_ride()
    
    assert result == "LOW_BATTERY"
    
    assert dead_scooter.is_locked == True
    
    