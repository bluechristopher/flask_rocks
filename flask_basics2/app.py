from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chickens")
def chicken_info():
    return render_template("chickens.html")

@app.route("/ducks")
def duck_info():
    return render_template("ducks.html")

@app.route("/pandas")
def panda_info():
    return render_template("pandas.html")

if __name__ == "__main__":
    app.run(debug=True, port=12345)
