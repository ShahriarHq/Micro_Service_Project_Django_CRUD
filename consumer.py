# amqps://vzjhuhne:uku10ys-OrFuw9XRb2QFAvjH8ychiyTC@gull.rmq.cloudamqp.com/vzjhuhne

import pika

params = pika.URLParameters('amqps://vzjhuhne:uku10ys-OrFuw9XRb2QFAvjH8ychiyTC@gull.rmq.cloudamqp.com/vzjhuhne')


connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("received in admin ")
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()