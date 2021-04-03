import json
from panini import app as panini_app

app = panini_app.App(
    service_name="request_for_location_history",
    host="127.0.0.1",
    port=4222,
)

log = app.logger

def _process(subject, message):
    print(f'processed {subject}: {message}')

@app.listen('process_aircraft_location_history')
async def process(msg):
    subject = msg.subject
    message = msg.data
    _process(subject, message)

if __name__ == "__main__":
    app.start()
