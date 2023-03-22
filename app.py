from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

messages = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form["message"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        messages.append((timestamp, message))

    messages_sorted = sorted(messages, key=lambda x: x[0], reverse=True)

    return render_template("index.html.jinja2", messages=messages_sorted)


if __name__ == "__main__":
    app.run(debug=True)