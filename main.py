from flask import Flask, render_template, request
from forms import LoginForm
# See https://wtforms.readthedocs.io/en/3.0.x/crash_course/
""" Command to check verion of Flask (from CLI) and WTForms respectively: 
    flask --version 
    pip freeze | grep WTForms
"""


app = Flask(__name__)
app.config['SECRET_KEY'] = '84da5b8a39a6d06bf8bc7a60cedcac93'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm(request.form)
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
