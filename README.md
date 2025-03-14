# RabbitMQ Queue Deletion Script

This repository contains a simple Python script that demonstrates how to connect to a RabbitMQ server using the [Pika](https://pika.readthedocs.io/) library and delete a specified queue.

## Overview

The script establishes a connection to RabbitMQ using an AMQP URL, deletes the specified queue, and then closes the connection. This is particularly useful for testing and maintenance purposes.

## Prerequisites

- **Python 3.x**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Pika Library**: Install Pika using pip:
  ```bash
  pip install pika
