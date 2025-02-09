import random
import json
import time
from google.cloud import pubsub_v1
 
# Google Cloud Pub/Sub configuration
PROJECT_ID = "<YOUR PROJECT ID>"
TOPIC_ID = "<YOUR PUB/SUB TOPIC ID>"
 
def generate_sales_data():
    """Generates random sales data."""
    return {
        "transaction_id": f"TXN{random.randint(100000, 999999)}",
        "product_id": f"PROD{random.randint(1000, 9999)}",
        "quantity": random.randint(1, 10),
        "sales_amount": round(random.uniform(10.0, 500.0), 2),
        "timestamp": time.time()
    }
 
def publish_to_pubsub(publisher, topic_path, data):
    """Publishes a batch of messages to a Pub/Sub topic."""
    try:
        for record in data:
            message = json.dumps(record).encode("utf-8")
            future = publisher.publish(topic_path, message)
            print(f"Published message ID: {future.result()}")
    except Exception as e:
        print(f"An error occurred: {e}")
 
def main():
    # Initialize Pub/Sub client
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)
    # Generate a batch of 5 records
    sales_data_batch = [generate_sales_data() for _ in range(5)]
    print(f"Generated batch of sales data:\n{json.dumps(sales_data_batch, indent=2)}")
    # Publish the batch to Pub/Sub
    publish_to_pubsub(publisher, topic_path, sales_data_batch)
    print(f"Published {len(sales_data_batch)} records to topic: {TOPIC_ID}")
 
if __name__ == "__main__":
    main()
