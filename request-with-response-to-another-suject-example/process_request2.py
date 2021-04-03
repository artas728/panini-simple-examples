import json
from panini import app as panini_app

app = panini_app.App(
    service_name="process_response",
    host="127.0.0.1",
    port=4222,
)

log = app.logger

def _process_request(subject, message):
    return f'processed {subject}: {message}'

@app.listen('aircraft_location_history_request.*')
async def request_listener(msg):
    subject = msg.subject
    message = msg.data
    result = _process_request(subject, message)
    return {'success': True, 'data': result}

if __name__ == "__main__":
    app.start()
