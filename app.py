from flask import Flask
import os.path
from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    def __str__(self):
        return f"Name:{self.first_name}, last:{self.last_name}"
    
    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        if request.method == "POST":
            first_name = request.form.get("fname")
            last_name = request.form.get("lname")
            p = Profile(first_name=first_name, last_name=last_name)
            db.session.add(p)
            db.session.commit()
            return f"{first_name} {last_name} "
        return render_template("signup.html")

@app.route("/homepage")
def homepage():
    users_data = Profile.query.all()
    return render_template("homepage.html", users_data=users_data)



@app.route('/')
def Hello_name():
    return f'hello {sys.argv[1]}'

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
