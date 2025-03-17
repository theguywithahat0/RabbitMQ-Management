import json
import os
import pika
import random
import time
from datetime import datetime

def publish_messages(num_messages=100, delay=0.1):
    """
    Publishes test messages to a RabbitMQ queue.

    The AMQP connection URL is taken from the environment variable AMQP_URL.
    Make sure you set it before running the script.

    Args:
        num_messages (int): The number of messages to publish.
        delay (float): Delay in seconds between publishing messages.
    """
    amqp_url = os.environ.get('AMQP_URL')
    if not amqp_url:
        raise ValueError("AMQP_URL environment variable not set. Please set it to your RabbitMQ connection URL.")

    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
    channel = connection.channel()

    # Create a durable queue
    queue_name = "rmq_cloudrun_test"
    channel.queue_declare(queue=queue_name, durable=True)

    # Define sample table/entity types
    table_types = ["User", "Bet", "Game", "Transaction", "Session"]

    for i in range(num_messages):
        table_type = random.choice(table_types)

        # Create data based on table type
        if table_type == "User":
            data = {
                "userId": random.randint(1000, 9999),
                "username": f"user_{random.randint(100, 999)}",
                "email": f"user{random.randint(100, 999)}@example.com",
                "active": random.random() > 0.2
            }
        elif table_type == "Bet":
            data = {
                "betId": random.randint(10000, 99999),
                "userId": random.randint(1000, 9999),
                "amount": round(random.uniform(10, 1000), 2),
                "odds": round(random.uniform(1.1, 10.0), 2),
                "timestamp": datetime.now().isoformat()
            }
        elif table_type == "Game":
            data = {
                "gameId": random.randint(100, 999),
                "name": f"Game_{random.randint(1, 100)}",
                "category": random.choice(["Sports", "Casino", "Poker", "Slots"]),
                "isActive": random.random() > 0.1
            }
        elif table_type == "Transaction":
            data = {
                "transactionId": f"TRX{random.randint(10000, 99999)}",
                "userId": random.randint(1000, 9999),
                "amount": round(random.uniform(10, 5000), 2),
                "type": random.choice(["deposit", "withdrawal", "bet", "win"]),
                "status": random.choice(["pending", "completed", "failed"]),
                "createdAt": datetime.now().isoformat()
            }
        else:  # Session
            data = {
                "sessionId": f"SES{random.randint(10000, 99999)}",
                "userId": random.randint(1000, 9999),
                "startTime": datetime.now().isoformat(),
                "ipAddress": f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}",
                "device": random.choice(["mobile", "desktop", "tablet"])
            }

        # Build the message structure
        message = {
            "Id": random.randint(10000, 99999),
            "EntityType": table_type,
            "Action": random.choice(["INSERT", "UPDATE", "DELETE"]),
            "Timestamp": datetime.now().isoformat(),
            "Data": data
        }

        # Publish the message (make it persistent)
        channel.basic_publish(
            exchange="",
            routing_key=queue_name,
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2)
        )

        print(f"Published message {i+1}: {table_type}")
        time.sleep(delay)

    connection.close()
    print("Completed sending test messages.")
