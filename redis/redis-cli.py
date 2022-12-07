import redis
import os

REDIS_HOST = 'localhost'
REDIS_PORT = "6379"

args = {
    "host": os.getenv('REDIS_HOST', ''),
    "port": os.getenv('REDIS_PORT', '')
}

# connect to redis
client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
#client.ping()
#print(f'connected to redis {REDIS_HOST}')

#r = redis.Redis(host='localhost',port=6379,db=0)

def is_redis_available(client):
    try:
        client.ping()
    except (redis.exceptions.ConnectionError, ConnectionRefusedError):
        print("Redis connection error!")
        return False
    return True

if is_redis_available(client):
    print(f'connected to redis {REDIS_HOST}')

# set a key for testing
client.set('name', 'jhon')

# get a value for testing
value = client.get('name')
#testing flush
client.flushall()
#value2 = client.get('test-key2')
print(value)
#print(value2)