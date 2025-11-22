CREATE TABLE sensors (
  id SERIAL PRIMARY KEY,
  mac VARCHAR(100),
  queue_timestamp BIGINT,
  sat_timestamp BIGINT,
  rssi INT,
  message TEXT,
  nodeId VARCHAR(255),
  source VARCHAR(100),
  received_at TIMESTAMP DEFAULT NOW()
);