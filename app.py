from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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
    
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Eco-Ride Control</title>
        </head>
        <body style="text-align: center; front-family: Arial, sans-serif; margin-top: 50px;">
            <h1>Управление Самокатом Eco-Ride </h1>
            <button id="start-btn" style="padding: 15px 30px; front-size: 18px; cursor: pointer; background-color: #4CAF50; color: White; border: none; border-radius: 5px;">
                Включить самокат
            </button>
            
            <script>
                const button = document.getElementById("start-btn");
                
                button.addEventListener('click', function() {
                    fetch ('/start', { method: 'POST' })
                    .then(response => response.json())
                    .then(data => {
                        if (data.result === 'RIDE_ACTIVE') {
                            button.innerText = 'Самокат включен(Поездка Активна)';
                            button.style.backgroundColor ='#2196F3';
                        }
                    });
            });
        </script>
    </body>
</html>
"""
    
@app.post("/start")
def start_scooter_ride():
    
    result = my_scooter.start_ride()
    
    return {
        "result": result,
        "is_locked": my_scooter.is_locked
    }