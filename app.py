from fastapi import FastAPI, Request
import psycopg2

app = FastAPI()

# Conexión a PostgreSQL
conn = psycopg2.connect(
    dbname="sensorsdb",
    user="postgres",
    password="tu_password",  # cámbialo por el tuyo
    host="localhost",
    port="5432"
)
conn.autocommit = True

@app.post("/sensors")
async def receive_sensor_data(request: Request):
    data = await request.json()
    mac = data.get("mac")
    queue_timestamp = data.get("queue_timestamp")
    sat_timestamp = data.get("sat_timestamp")
    rssi = data.get("rssi")
    message = data.get("message")
    nodeId = data.get("nodeId")
    source = data.get("source")

    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO sensors(mac, queue_timestamp, sat_timestamp, rssi, message, nodeId, source, received_at)
            VALUES (%s,%s,%s,%s,%s,%s,%s,NOW())
            """,
            (mac, queue_timestamp, sat_timestamp, rssi, message, nodeId, source)
        )

    return {"status": "ok"}