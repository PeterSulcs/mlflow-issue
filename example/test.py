import requests

r = requests.get("https://127.0.0.1:9000", auth=("minio", "minio123"))
print(r)
print(r.content)