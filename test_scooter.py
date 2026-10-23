import pytest

from Scooter import Scooter


@pytest.fixture

def default_scooter():
    return Scooter(80, 10, True)

def test_scooter_ride(default_scooter):
    
    result = default_scooter.start_ride()
    
    assert result == "RIDE_ACTIVE"
    
    assert default_scooter.is_locked == False
    
def test_scooter_low_battery(default_scooter):
    
    default_scooter.battery = 0
    
    result = default_scooter.start_ride()
    
    assert result == "LOW_BATTERY"
    
    assert default_scooter.is_locked == True
    
    