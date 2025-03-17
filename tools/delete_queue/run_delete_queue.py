#!/usr/bin/env python3
import argparse
from delete_queue import delete_queue

def parse_args():
    parser = argparse.ArgumentParser(description="Delete a RabbitMQ queue.")
    parser.add_argument("--queue", type=str, required=True,
                        help="Name of the queue to delete.")
    return parser.parse_args()

def main():
    args = parse_args()
    delete_queue(args.queue)

if __name__ == '__main__':
    main()
