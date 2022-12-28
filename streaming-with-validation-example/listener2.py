from panini import app as panini_app
from models import AircraftLocation
app = panini_app.App(
    service_name="listener_with_validators",
    host="127.0.0.1",
    port=4222,
)

log = app.logger



@app.listen('aircraft_live_location.us.east.>', data_type=AircraftLocation)
async def receive_messages(msg):
    subject = msg.subject
    data = msg.data
    log.info(f"got msg {subject}:{data}")

if __name__ == "__main__":
    app.start()
