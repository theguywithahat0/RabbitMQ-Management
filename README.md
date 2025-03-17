# RabbitMQ Queue Management Tools

A collection of Python utilities for managing RabbitMQ queues using the [Pika](https://pika.readthedocs.io/) library.

## Overview

RabbitMQ is a powerful message broker implementing the Advanced Message Queuing Protocol (AMQP). While RabbitMQ provides a management UI, programmatic access is often needed for automation, testing, and maintenance workflows.

This toolkit includes:
- **Queue Deletion Tool**: Safely remove queues from your RabbitMQ server
- **Message Publisher**: Generate and publish test messages to RabbitMQ queues

## Use Cases

- **Test Environment Cleanup**: Easily clean up test queues after running integration tests
- **Load Testing**: Generate sample messages with configurable volume and delay
- **Maintenance Operations**: Programmatically manage queues during system maintenance
- **DevOps Automation**: Incorporate into CI/CD pipelines for environment management
- **Troubleshooting**: Quickly reset queues during debugging sessions

## Prerequisites

- **Python 3.6+**: Available from [python.org](https://www.python.org/downloads/)
- **Pika Library**: Install with `pip install pika`
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

   Alternatively, create and use a `requirements.txt` file:
   ```
   pika>=1.2.0
   ```
   
   And install with:
   ```bash
   pip install -r requirements.txt
   ```

## Tools

### Queue Deletion

Delete a RabbitMQ queue with a simple command:

```bash
# Set your RabbitMQ connection string
export AMQP_URL="amqps://username:password@host/vhost"

# Run the deletion tool
python -m tools.delete_queue.run_delete_queue --queue queue_name
```

### Message Publisher

Generate and publish test messages to a RabbitMQ queue:

```bash
# Set your RabbitMQ connection string
export AMQP_URL="amqps://username:password@host/vhost"

# Run the publisher with default settings (100 messages, 0.1s delay)
python -m tools.rmq_publisher.run_publisher

# Or customize the number of messages and delay
python -m tools.rmq_publisher.run_publisher --num-messages 500 --delay 0.05
```

The publisher generates realistic test data for various entity types:
- Users
- Bets
- Games
- Transactions
- Sessions

Each message contains randomly generated data appropriate for the entity type, along with metadata such as action type (INSERT, UPDATE, DELETE) and timestamps.

## Security Considerations

- Store sensitive connection details in environment variables rather than hardcoding
- Use TLS connections (amqps://) in production environments
- Create dedicated RabbitMQ users with minimal required permissions
- Be cautious when deleting queues in production environments

## Future Enhancements

- Queue creation utilities
- Queue monitoring tools
- Batch operations for multiple queues
- Exchange management
- User management
- Message consumption and processing tools

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
