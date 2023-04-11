# EXAMPLE: set_and_get
# HIDE_START
import redis
# REMOVE_START
import pytest
# REMOVE_END

def run():
  
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
  # REMOVE_START
  assert True == status
  assert 'Process 134' == value

@pytest.mark.doc
def test_set_and_get():
  run()
# REMOVE_END