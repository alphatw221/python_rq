from rq import Retry
from redis import Redis
from rq import Queue
import requests
# import datetime
from rq import use_connection


from work1 import working_function

def main():
    conn = Redis('127.0.0.1', 6379)
    conn = Redis('localhost',6379)
    conn = Redis()
    # use_connection(connection)
    queue = Queue(connection=conn)
    result = queue.enqueue(working_function, kwargs={
                    'text': 'testing'}, description="test")

    print(result)
    # job = queue.enqueue_at(datetime(2019, 10, 8, 9, 15), say_hello)
    # # Schedule job to be run in 10 seconds
    # job = queue.enqueue_in(timedelta(seconds=10), say_hello)
    # # Retry up to 3 times, failed job will be requeued immediately
    # queue.enqueue(say_hello, retry=Retry(max=3))
    # # Retry up to 3 times, with configurable intervals between retries
    # queue.enqueue(say_hello, retry=Retry(max=3, interval=[10, 30, 60]))

if __name__ == "__main__":
    main()