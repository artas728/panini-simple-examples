from panini import app as panini_app
from panini.validator import Validator, Field

app = panini_app.App(
    service_name="listener_with_validators",
    host="127.0.0.1",
    port=4222,
)

log = app.logger

class _DepartureArrivalValiator(Validator):
    airport = Field(type=str)
    timezone = Field(type=str)
    iata = Field(type=str)
    icao = Field(type=str)
    terminal = Field(type=str)
    gate = Field(type=str)
    delay = Field(type=int)
    scheduled = Field(type=str)
    estimated = Field(type=str)
    actual = Field(type=str, null=True)
    estimated_runway = Field(type=str, null=True)
    actual_runway = Field(type=str, null=True)

class _AirlineValidator(Validator):
    name = Field(type=str)
    iata = Field(type=str)
    icao = Field(type=str)

class _FlightValidator(Validator):
    number = Field(type=str)
    iata = Field(type=str)
    icao = Field(type=str)
    codeshared = Field(type=str, null=True)

class _AircraftValidator(Validator):
    registration = Field(type=str)
    iata = Field(type=str)
    icao = Field(type=str)
    icao24 = Field(type=str)

class _LiveValidator(Validator):
    updated = Field(type=str)
    latitude = Field(type=float)
    longitude = Field(type=float)
    altitude = Field(type=float)
    direction = Field(type=float)
    speed_horizontal = Field(type=float)
    speed_vertical = Field(type=float)
    is_ground = Field(type=bool)

class AircraftLocationValidator(Validator):
    flight_date = Field(type=str)
    flight_status = Field(type=str, default='Unknown')
    departure = Field(type=_DepartureArrivalValiator)
    arrival = Field(type=_DepartureArrivalValiator)
    airline = Field(type=_AirlineValidator)
    flight = Field(type=_FlightValidator)
    aircraft = Field(type=_AircraftValidator)
    live = Field(type=_LiveValidator)

@app.listen('aircraft_live_location.us.east.>', validator=AircraftLocationValidator)
async def receive_messages(msg):
    subject = msg.subject
    data = msg.data
    log.info(f"got msg {subject}:{data}")

if __name__ == "__main__":
    app.start()
