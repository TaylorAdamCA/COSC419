from flask import Flask, render_template, Markup, request, flash, redirect, url_for, session
from flask_login import LoginManager, login_required, UserMixin, login_user
from wtforms import Form, PasswordField, StringField, validators, ValidationError
# from passlib.hash import sha256_crypt
import random
from flask_sqlalchemy import SQLAlchemy

MyApp = Flask(__name__)

MyApp.config.from_pyfile('config.py')

db = SQLAlchemy(MyApp)
login_manager = LoginManager(MyApp)


class users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100))

    def __repr__(self):
        return '<User %r>' % self.username
@MyApp.route("/")
def template():
    return render_template("index.html")


@MyApp.errorhandler(403)
def forbiddenerror():
    return render_template('403_page.html'), 403


def validate_user(form, username):
    if users.query.filter_by(username=username.data).first():
        raise ValidationError('Username already exists')
def validate_email(form, email):
    if users.query.filter_by(email=email.data).first():
        raise ValidationError('Email already exists')

class Register(Form):
    username = StringField(
        'UserName:', [
            validators.Required(), validate_user])
    email = StringField(
        'Email:', [
            validators.Email(
                message=('Not a valid email.')), validate_email])
    password = PasswordField(
        'Password:', [
            validators.DataRequired(), validators.EqualTo(
                'confirm', message=('Passwords must match'))])
    confirm = PasswordField('Confirm:')



@MyApp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remeber=form.remeber.check)
            return redirect(url_for('welcome'))
        else:
            flash('Login Unsuccessful.')

    return render_template('login.html',
                           form=form)

@MyApp.route("/welcome")
@login_required
def welcome():
  return render_template('welcome.html')


@MyApp.route("/register", methods=['GET', 'POST'])
def register():
    form = Register(request.form)
    if request.method == 'POST' and form.validate():
        user = users(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data)
        db.session.add(user)
        db.session.commit()
        redirect('login')
    return render_template('register.html', form=form)




@login_manager.user_loader
def load_user(user_id):
    return users.query.get(int(user_id))


if __name__ == "__main__":
    MyApp.run()

