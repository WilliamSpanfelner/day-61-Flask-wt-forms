from flask import Flask, render_template, request
from wtforms import Form, StringField

# See https://wtforms.readthedocs.io/en/3.0.x/crash_course/

app = Flask(__name__)


# Create the login form object
class LoginForm(Form):
    email = StringField("Email")
    password = StringField("Password")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    form = LoginForm(request.form)
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
