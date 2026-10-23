from fastapi import FastAPI
from Scooter import Scooter

app = FastAPI()

my_scooter = Scooter(battery=90, milleage=15, is_locked=True)

@app.get("/status")
def get_scooter_status():
    return {
        "Battery": my_scooter.battery,
        "milleage": my_scooter.milleage,
        "is_locked": my_scooter.is_locked
    }
    
@app.post("/start")
def start_scooter_ride():
    
    result = my_scooter.start_ride()
    
    return {
        "result": result,
        "is_locked": my_scooter.is_locked
    }