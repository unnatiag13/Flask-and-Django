from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "supersecretkey"  # required for flash messages

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        flash("✅ User saved successfully!", "success")
        return redirect('/')

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
