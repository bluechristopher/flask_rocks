from flask import Flask, render_template

app = Flask(__name__)

# staff information
staff_data = {
    "kkl": {"name": "Mr Kan Kok Leong", "gender": "M", "dept": "Math"},
    "jy": {"name": "Mr Joshua Yeo", "gender": "M", "dept": "Physics"},
    "dl": {"name": "Mr Desmond Lee", "gender": "M", "dept": "Math"},
    "gsc": {"name": "Mr Gi Soong Chee", "gender": "M", "dept": "Computing"},
    "al": {"name": "Mr Andy Lim", "gender": "M", "dept": "PW"},
    "tlr": {"name": "Ms Tan Li Rong", "gender": "F", "dept": "Math"},
    "csy": {"name": "Mr Chang Shu Yuet", "gender": "M", "dept": "PE"},
    "lmh": {"name": "Mr Lam Meng Hwee", "gender": "M", "dept": "Math"},
    "ks": {"name": "Mr Kelvin Soo", "gender": "M", "dept": "Physics"},
    "kwt": {"name": "Ms Koh Wenting", "gender": "F", "dept": "PW"}
}

@app.route("/")
def home():
    return render_template("index.html", staff_data=staff_data)


if __name__ == "__main__":
    app.run(debug=True)
