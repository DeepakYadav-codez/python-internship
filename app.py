from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["username"]
    return f"<h2>Hello, {name}! Thanks for submitting.</h2>"

if __name__ == "__main__":
    app.run(debug=True)
