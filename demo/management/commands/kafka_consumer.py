# tracker/management/commands/kafka_consumer.py
from django.core.management.base import BaseCommand
from confluent_kafka import Consumer, KafkaException
import json
from demo.models import LocationUpdate
import os
from collections import defaultdict
from demo.models import Post
from django.db import transaction

class Command(BaseCommand):
    help = 'Run Kafka consumer to listen for location updates'

    def process_batch(self,like_batch):
        print(f"Batch processing Started! {like_batch}")
        with transaction.atomic():
            for post_id, like_count in like_batch.items():
                post = Post.objects.select_for_update().get(id=post_id)
                post.likes += like_count
                print("Post count updated")
                post.save()

    def handle(self, *args, **options):
        like_batch = defaultdict(int)
        print(like_batch)
        conf = {
            'bootstrap.servers': os.getenv('KAFKA_BROKER_URL', 'localhost:9092'),
            'group.id': "location_group",
            'auto.offset.reset': 'earliest'
        }

        consumer = Consumer(conf)
        #consumer.subscribe(['location_updates'])
        consumer.subscribe(['like_topic'])
        print("KAFKA CONSUMER STARTED")
        total_messages = 0
        try:
            while True:
               
                msg = consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    print(msg.error())
                    #break
                    continue

                data = json.loads(msg.value().decode('utf-8'))
                post_id = data['post_id']
                like_batch[post_id] += 1
                total_messages += 1
                print(like_batch, len(like_batch),total_messages)
                if total_messages >= 1000:  # For example, process every 1000 messages
                    self.process_batch(like_batch)
                    like_batch.clear()
                    total_messages = 0


        except KeyboardInterrupt:
            pass
        finally:
            consumer.close()
