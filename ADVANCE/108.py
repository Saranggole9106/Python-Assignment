import requests

# URL of a public API
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(f"Title: {data['title']}")
else:
    print("Failed to retrieve data.")
