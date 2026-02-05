from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "name": "Unnati",
        "role": "AI & ML Student",
        "skills": ["Python", "Flask", "Machine Learning", "Power BI"]
    }
    return render_template("index.html", data=data)

@app.route("/hello/<username>")
def hello(username):
    return render_template(
        "index.html",
        data={
            "name": username,
            "role": "Guest User",
            "skills": ["Exploring Flask 🚀"]
        }
    )

if __name__ == "__main__":
    app.run(debug=True)
