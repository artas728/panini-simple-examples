from pydantic import BaseModel



class _DepartureArrival(BaseModel):
    airport: str
    timezone: str
    iata: str
    icao: str
    terminal: str
    gate: str
    delay: int
    scheduled: str
    estimated: str
    actual: str = None
    estimated_runway: str = None
    actual_runway:str = None

class _Airline(BaseModel):
    name: str
    iata: str
    icao: str

class _Flight(BaseModel):
    number: str
    iata: str
    icao: str = None

class _Aircraft(BaseModel):
    registration: str
    iata: str
    icao: str
    icao24: str

class _Live(BaseModel):
    updated: str
    latitude: float
    longitude: float
    altitude: float
    direction: float
    speed_horizontal: float
    speed_vertical: float
    is_ground: bool

class AircraftLocation(BaseModel):
    flight_date: str
    flight_status: str = 'Unknown'
    departure: _DepartureArrival
    arrival: _DepartureArrival
    airline: _Airline
    flight: _Flight
    aircraft: _Aircraft
    live: _Live