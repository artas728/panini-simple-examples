from panini import app as panini_app

app = panini_app.App(
    service_name="listener",
    host="127.0.0.1",
    port=4222,
)

log = app.logger

@app.listen('aircraft_live_location.us.east.>')
async def receive_messages(msg):
    subject = msg.subject
    data = msg.data
    log.info(f"got msg {subject}:{data}")

if __name__ == "__main__":
    app.start()
