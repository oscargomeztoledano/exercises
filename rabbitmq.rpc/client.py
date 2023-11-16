#!/usr/bin/python3

import pika
import uuid
import sys


class FactorialRpcClient(object):
    def __init__(self):
        localhost = pika.ConnectionParameters(host='localhost')
        self.connection = pika.BlockingConnection(localhost)
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            on_message_callback=self.on_response,
            auto_ack=False,
            queue=self.callback_queue
        )

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            body=str(n),
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            )
        )

        while self.response is None:
            self.connection.process_data_events()

        return int(self.response)

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} [int] (10 max)")
    sys.exit(1)

if not sys.argv[1].isdigit() or int(sys.argv[1]) > 10:
    print(" [!] Please provide an integer as argument, 10 max")
    sys.exit(1)

client = FactorialRpcClient()

print(" [x] Requesting factorial(%d)" % int(sys.argv[1]))
response = client.call(int(sys.argv[1]))
print(" [.] Got %r" % response)
