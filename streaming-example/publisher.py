from panini import app as panini_app

app = panini_app.App(
    service_name="publisher",
    host="127.0.0.1",
    port=4222,
)

def get_some_aircraft_location_update():
    return {
    "key1": "value1",
    "key2": 2,
    "key3": 3.0,
    "key4": [1, 2, 3, 4],
    "key5": {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5},
    "key6": {"subkey1": "1", "subkey2": 2, "3": 3, "4": 4, "5": 5},
    "key7": None,
}

@app.timer_task(interval=1)
async def publish():
    message = get_some_aircraft_location_update()
    await app.publish(subject='aircraft_live_location.us.east.atlanta.FL422', message=message)

if __name__ == "__main__":
    app.start()
