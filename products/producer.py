# amqps://vzjhuhne:uku10ys-OrFuw9XRb2QFAvjH8ychiyTC@gull.rmq.cloudamqp.com/vzjhuhne

import pika,json

params = pika.URLParameters('amqps://vzjhuhne:uku10ys-OrFuw9XRb2QFAvjH8ychiyTC@gull.rmq.cloudamqp.com/vzjhuhne')


connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method,body):
    properties = pika.BasicProperties(method)

    channel.basic_publish(exchange='', routing_key='main_db',body=json.dumps(body),properties=properties)