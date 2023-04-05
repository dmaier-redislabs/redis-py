# HIDE_START
import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)
# HIDE_END

status = r.set('bike:1', 'Process 134')

if status == True:
  print('Successfully added a bike.')

value = r.get('bike:1')

if value:
  print('The name of the bike is: {}.'.format(value))
