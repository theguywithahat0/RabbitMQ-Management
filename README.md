# RabbitMQ Queue Management Tools

This repository contains Python utilities for managing RabbitMQ queues using the [Pika](https://pika.readthedocs.io/) library. These tools help simplify common RabbitMQ administration tasks.

## Overview

RabbitMQ is a powerful message broker that implements the Advanced Message Queuing Protocol (AMQP). While RabbitMQ provides a management UI, programmatic access is often needed for automation, testing, and maintenance workflows.

This toolkit currently includes:
- Queue deletion script: Safely remove queues from your RabbitMQ server

## Use Cases

- **Test Environment Cleanup**: Easily clean up test queues after running integration tests
- **Maintenance Operations**: Programmatically manage queues during system maintenance
- **DevOps Automation**: Incorporate into CI/CD pipelines for environment management
- **Troubleshooting**: Quickly reset queues during debugging sessions

## Prerequisites

- **Python 3.6+**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Pika Library**: Install Pika using pip:
  ```bash
  pip install pika
  ```
- **RabbitMQ Server**: Access to a RabbitMQ instance with appropriate permissions

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/rabbitmq-management.git
   cd rabbitmq-management
   ```

2. Install the required dependencies:
   ```bash
   pip install pika
   ```

   Alternatively, you can create a `requirements.txt` file with the following content:
   ```
   pika>=1.2.0
   ```
   
   And then install using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Queue Deletion

To delete a RabbitMQ queue:

1. Edit `delete_queue.py` with your connection details and queue name:
   ```python
   amqp_url = "amqps://username:password@host/vhost"
   queue_name = "queue_to_delete"
   ```

2. Run the script:
   ```bash
   python delete_queue.py
   ```

## Security Considerations

- Store sensitive connection details in environment variables or a secure configuration file
- Use TLS connections (amqps://) in production environments
- Create dedicated users with minimal required permissions

## Future Enhancements

- Queue creation utilities
- Queue monitoring tools
- Batch operations for multiple queues
- Exchange management
- User management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
