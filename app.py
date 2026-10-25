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
            
            <button id="stop-btn" style="padding: 15px 30px; front-size: 18px; cursor: pointer; background-color: #4CAF50; color: White; border: none; border-radius: 5px;">
            Закончить поездку
            </button>
            
            <script>
                const startBtn = document.getElementById("start-btn");
                startBtn.addEventListener('click', function() {
                    fetch('/start', { method: 'POST' })
                    .then(response => response.json())
                    .then(data => {
                        if (data.result === 'RIDE_ACTIVE') {
                            startBtn.innerText = 'Самокат включен (Поездка Активна) 🟢';
                            startBtn.style.backgroundColor = '#2196F3';
                        }
                    });
                });

                const stopBtn = document.getElementById("stop-btn");
                stopBtn.addEventListener('click', function() {
                    fetch('/end', { method: 'POST' })
                    .then(response => response.json())
                    .then(data => {
                        if (data.result === 'READY') {
                            stopBtn.innerText = 'Поездка окончена 🛑';
                            stopBtn.style.backgroundColor = '#f44336'; 
                            
                            startBtn.innerText = 'Включить самокат';
                            startBtn.style.backgroundColor = '#4CAF50';
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
    
@app.post("/end")
def stop_scooter_ride():
    
    result = my_scooter.stop_ride()
    
    return {
        "result": result,
        "is_locked": my_scooter.is_locked
    }