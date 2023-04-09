import os.path
from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
import subprocess

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_site.db'
# ALLOWED_EXTENSIONS = ["png", "jpeg", "jpg", "gif"]
# def allowed_file(filename):
#      return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)

    def __str__(self):
        return f"Name:{self.first_name}, Last:{self.last_name}"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        p = Profile(first_name=first_name, last_name=last_name)
        db.session.add(p)
        db.session.commit()
        return redirect('/homepage')
        # return f"{first_name} {last_name} "
    return render_template("signup.html")

@app.route("/homepage")
def homepage():
    users_data = Profile.query.all()
    return render_template("homepage.html", users_data=users_data)

@app.route("/docker", methods=["GET", "POST"])
def docker():
    if request.method == "POST":
        image_name = request.form.get("image_name")
        subprocess.run(['docker', 'build', '-t', f"{image_name}", '.'])
        subprocess.run(['git', 'init'])
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', f"Pushing {image_name} Docker image to GitHub"])
        subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/<username>/<repo_name>.git'])
        subprocess.run(['git', 'push', '-u', 'origin', 'master'])
        return f"Docker image {image_name} created and pushed to GitHub"
    return render_template("docker.html")

    

if __name__ == "__main__":
    app.run(debug=True)


