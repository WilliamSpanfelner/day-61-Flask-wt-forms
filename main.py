from flask import Flask, render_template, request, redirect
from forms import LoginForm
from flask_bootstrap import Bootstrap
# See https://wtforms.readthedocs.io/en/3.0.x/crash_course/
""" Command to check verion of Flask (from CLI) and WTForms respectively: 
    flask --version 
    pip freeze | grep WTForms
"""


app = Flask(__name__)
app.config['SECRET_KEY'] = '84da5b8a39a6d06bf8bc7a60cedcac93'
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm(request.form)
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
