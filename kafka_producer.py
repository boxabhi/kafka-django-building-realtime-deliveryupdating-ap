# kafka_producer.py
from confluent_kafka import Producer
import json
import time
import os

# Initialize Kafka Producer
conf = {'bootstrap.servers': os.getenv('KAFKA_BROKER_URL', 'localhost:9092')}
producer = Producer(**conf)

# Define start and end coordinates for the road
start_latitude = 19.0760
start_longitude = 72.8777
end_latitude = 18.5204
end_longitude = 73.8567

# Number of steps and initial position
num_steps = 1000  # Increased number of steps for smoother movement
step_size_lat = (end_latitude - start_latitude) / num_steps
step_size_lon = (end_longitude - start_longitude) / num_steps
current_step = 0

# Function to handle message delivery report
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

topic = "like_topic"

while True:
    # Calculate current position
    latitude = start_latitude + step_size_lat * current_step
    longitude = start_longitude + step_size_lon * current_step
    
    # Create location data
    data = {
        'latitude': latitude,
        'longitude': longitude
    }
    
    # Produce the message to Kafka
    producer.produce(topic, json.dumps(data).encode('utf-8'), callback=delivery_report)
    producer.flush()
    
    # Update step count
    current_step += 1
    if current_step > num_steps:
        current_step = 0  # Loop the simulation

    # Sleep for 2 seconds to simulate a more realistic speed
    time.sleep(2)
