from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ar")
def ar():
    return render_template("ar.html")

@app.route("/smg")
def smg():
    return render_template("smg.html")


@app.route("/sg")
def sg():
    return render_template("sg.html")

@app.route("/sr")
def sr():
    return render_template("sr.html")

@app.route("/lmg")
def lmg():
    return render_template("lmg.html")

@app.route("/mm")
def mm():
    return render_template("mm.html")

@app.route("/pistol")
def pistol():
    return render_template("pistol.html")

if __name__ == "__main__":
    app.run(debug=True)