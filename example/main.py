from flask import Flask
from flask import request, render_template

from pyppesnap import get_snapshot_by_url

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/get_web", methods=["POST"])
def get_web():
    if request.method == "POST":
        web_address = request.form.get("web_address")
        screenshot = get_snapshot_by_url(web_address)
        return screenshot


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9898, debug=True)
