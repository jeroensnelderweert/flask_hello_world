from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")


def calculate_weeknumber():
    date = datetime.datetime.now()
    week_number = date.isocalendar().week
    return f"Week number is: {week_number}"

if __name__ == "__main__":
    app.run()