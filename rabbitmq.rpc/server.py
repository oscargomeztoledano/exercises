#!/usr/bin/python3

import pika


localhost = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(localhost)
channel = connection.channel()

channel.queue_delete(queue='rpc_queue')
channel.queue_declare(queue='rpc_queue')


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] factorial(%s)" % n)
    response = factorial(n)

    properties = pika.BasicProperties(
        correlation_id=props.correlation_id
    )

    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=properties,
        body=str(response)
    )

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    on_message_callback=on_request,
    queue='rpc_queue'
)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
