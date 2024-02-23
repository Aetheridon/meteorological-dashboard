import os

from parse_data import parse_data
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():

    if request.method == "POST":
        images = ["pics/" + image for image in os.listdir("static/pics")]
        parse_data()
        return render_template("index.html", images=images)

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run()