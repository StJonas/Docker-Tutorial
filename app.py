from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis
r = redis.Redis(host="redis", port=6379)

# Define the file path
file_path = "/data/message.txt"


@app.route("/")
def hello():
    # Increment the counter
    count = r.incr("hello_count")

    # Set a value in Redis
    r.set("welcome", "\n<h1>Welcome to the Docker Tutorial!</h1>")

    # Retrieve the value from Redis
    welcome = r.get("welcome").decode("utf-8")

    # Write the message and count to a file
    with open(file_path, "w") as file:
        file.write(f"{welcome}\nHello has been called {count} times.")

    with open(file_path, "r") as file:
        file_content = file.read()

    return f"{file_content}"


@app.route("/read-file")
def read_file():
    try:
        # Check if the file exists, read it and return its contents
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()
            return f"{content}"
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
