from panini import app as panini_app
from models import AircraftLocation

app = panini_app.App(
    service_name="publisher",
    host="127.0.0.1",
    port=4222,
)


def get_some_aircraft_location_update():
    return {
            "flight_date": "2020-12-12",
            "flight_status": "active",
            "departure": {
                "airport": "Atlanta International",
                "timezone": "America/New_York",
                "iata": "SFO",
                "icao": "KSFO",
                "terminal": "2",
                "gate": "D11",
                "delay": 13,
                "scheduled": "2020-12-12T04:20:00+00:00",
                "estimated": "2020-12-12T04:20:00+00:00",
                "actual": "2020-12-12T04:20:13+00:00",
                "estimated_runway": "2020-12-12T04:20:13+00:00",
                "actual_runway": "2020-12-12T04:20:13+00:00"
            },
            "arrival": {
                "airport": "Dallas/Fort Worth International",
                "timezone": "America/Chicago",
                "iata": "DFW",
                "icao": "KDFW",
                "terminal": "A",
                "gate": "A22",
                "baggage": "A17",
                "delay": 0,
                "scheduled": "2020-12-12T04:20:00+00:00",
                "estimated": "2020-12-12T04:20:00+00:00",
                "actual": None,
                "estimated_runway": None,
                "actual_runway": None
            },
            "airline": {
                "name": "American Airlines",
                "iata": "AA",
                "icao": "AAL"
            },
            "flight": {
                "number": "1004",
                "iata": "AA1004",
                "icao": "AAL1004",
                "codeshared": None
            },
            "aircraft": {
               "registration": "N160AN",
               "iata": "A321",
               "icao": "A321",
               "icao24": "A0F1BB"
            },
            "live": {
                "updated": "2020-12-12T10:00:00+00:00",
                "latitude": 36.28560000,
                "longitude": -106.80700000,
                "altitude": 8846.820,
                "direction": 114.340,
                "speed_horizontal": 894.348,
                "speed_vertical": 1.188,
                "is_ground": False
            }
}

@app.task(interval=1)
async def publish():
    message_dict = get_some_aircraft_location_update()
    message_model = AircraftLocation(**message_dict)
    await app.publish(subject='aircraft_live_location.us.east.atlanta.FL422', message=message_model)

if __name__ == "__main__":
    app.start()
