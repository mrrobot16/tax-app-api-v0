import requests
import time

# The URL to test
url = "https://tax-app-api-dev-004c410e86db.herokuapp.com"

# Number of requests to send
number_of_requests = 100

# Store the response times
response_times = []

print(f"Sending {number_of_requests} requests to {url}...")

for i in range(number_of_requests):
    start_time = time.time()
    response = requests.get(url)
    response_time = time.time() - start_time
    response_times.append(response_time)
    print(f"Request {i+1}: Response time = {response_time:.3f} seconds, Status Code = {response.status_code}")

average_response_time = sum(response_times) / len(response_times)
print(f"Average response time: {average_response_time:.3f} seconds")

