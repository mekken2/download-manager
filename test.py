import requests

payload = "simple-multithreaded-download-manager-in-python/"
r = requests.get('https://www.geeksforgeeks.org/', params=payload)
print(r.url)

print(r.content.json())