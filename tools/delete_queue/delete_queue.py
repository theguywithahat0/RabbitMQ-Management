import os
import pika

def delete_queue(queue_name):
    """
    Deletes the specified RabbitMQ queue.

    The AMQP connection URL is taken from the environment variable AMQP_URL.
    
    Args:
        queue_name (str): The name of the queue to delete.
    """
    amqp_url = os.environ.get('AMQP_URL')
    if not amqp_url:
        raise ValueError("AMQP_URL environment variable not set. Please set it to your RabbitMQ connection URL.")

    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
    channel = connection.channel()

    # Delete the queue
    channel.queue_delete(queue=queue_name)
    connection.close()
    
    print(f"Queue '{queue_name}' deleted.")
