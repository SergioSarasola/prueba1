import os
import psycopg2
from fastapi import FastAPI, Request

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL no está definida. Configura la variable de entorno antes de arrancar la app.")

conn = psycopg2.connect(DATABASE_URL)
conn.autocommit = True

@app.post("/sensors")
async def receive_sensor_data(request: Request):
    data = await request.json()
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO sensors(mac, queue_timestamp, sat_timestamp, rssi, message, nodeId, source, received_at)
            VALUES (%s,%s,%s,%s,%s,%s,%s,NOW())
            """,
            (
                data["mac"], data["queue_timestamp"], data["sat_timestamp"],
                data["rssi"], data["message"], data["nodeId"], data["source"]
            )
        )
    return {"status": "ok"}