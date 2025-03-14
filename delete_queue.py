import pika

# Replace the placeholders with your actual connection details
amqp_url = "amqps://<username>:<password>@<host>/<vhost>"

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
channel = connection.channel()

# Specify the name of the queue you want to delete
queue_name = "<your_queue_name>"

# Delete the queue
channel.queue_delete(queue=queue_name)
connection.close()

print(queue_name, "Queue deleted")
