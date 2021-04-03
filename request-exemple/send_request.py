import json
from panini import app as panini_app

app = panini_app.App(
    service_name="request_for_location_history",
    host="127.0.0.1",
    port=4222,
)

log = app.logger

@app.timer_task(interval=1)
async def request_location_history():
    response = await app.request(subject='aircraft_location_history_request.AA1004', message={'from':1585943864})
    log.info(f'response: {response}')

if __name__ == "__main__":
    app.start()
