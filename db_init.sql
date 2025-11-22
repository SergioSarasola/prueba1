CREATE DATABASE sensorsdb;

\c sensorsdb;

CREATE TABLE sensors (
  id SERIAL PRIMARY KEY,
  mac VARCHAR(50),
  queue_timestamp BIGINT,
  sat_timestamp BIGINT,
  rssi INT,
  message TEXT,
  nodeId VARCHAR(100),
  source VARCHAR(50),
  received_at TIMESTAMP DEFAULT NOW()
);