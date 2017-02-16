from prometheus_client import start_http_server, Summary, Gauge
import random
import time


# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
g = Gauge('fridge_temperature', 'Temperatur of the fridge')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

def count(t):
  g.inc()
  time.sleep(t)
  

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        r = random.random()
        process_request(r)
        count(r)

