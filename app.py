from flask import Flask
import os.path
from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
import sys
import subprocess

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
    
@app.route("/docker", methods=["GET", "POST"])
def docker():
    if request.method == "POST":
        image_name = request.form.get("image_name")
        subprocess.run(['docker', 'build', '-t', f"{image_name}", '.'])
        subprocess.run(['git', 'init'])
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', f"Pushing {image_name} Docker image to GitHub"])
        subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/NextGen20/flaskproject.git'])
        subprocess.run(['git', 'push', '-u', 'origin', 'main'])
        return f"Docker image {image_name} created and pushed to GitHub"
    return render_template("docker.html")

@app.route("/homepage")
def homepage():
    users_data = Profile.query.all()
    return render_template("homepage.html", users_data=users_data)



@app.route('/')
def Hello_name():
    return f'hello {sys.argv[1]}'

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
