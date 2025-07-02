# app/app.py
from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUEST_COUNT = Counter("request_count", "App Request Count")

@app.route("/")
def hello():
    REQUEST_COUNT.inc()
    return "Hello, prometheus!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    prometheus_client.start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)
