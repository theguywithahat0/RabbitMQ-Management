#!/usr/bin/env python3
import argparse
from rmq_publisher import publisher

def parse_args():
    parser = argparse.ArgumentParser(description="Publish test messages to RabbitMQ.")
    parser.add_argument("--num-messages", type=int, default=100,
                        help="Number of messages to publish (default: 100).")
    parser.add_argument("--delay", type=float, default=0.1,
                        help="Delay in seconds between messages (default: 0.1).")
    return parser.parse_args()

def main():
    args = parse_args()
    publisher.publish_messages(num_messages=args.num_messages, delay=args.delay)

if __name__ == '__main__':
    main()
