import asyncio
import os

PROJECT_NAME = 'UGC Api'

KAFKA_HOST = os.getenv('KAFKA_HOST')
KAFKA_PORT = int(os.getenv('KAFKA_PORT', 9092))
KAFKA_TOPIC = 'rating'
KAFKA_RATING_CLIENT_ID = 'ugc_rating'
KAFKA_CONSUMER_GROUP = 'group-id'
SENTRY_SDK_DSN = os.getenv('SENTRY_SDK_DSN')
loop = asyncio.get_event_loop()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
