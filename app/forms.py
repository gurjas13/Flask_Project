from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , BooleanField , TextAreaField
from wtforms.validators import DataRequired,length,Email,equal_to,ValidationError
from app.models import User,Post

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired() ,length(min=2,max=10) ])
    email = StringField('Email' , validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),equal_to('password')])
    submit = SubmitField('Sign Up')

    def validate_username (self, username):
        user = User.query.filter_by(username= username.data).first()
        if user:
            raise ValidationError('This username already exists')

    def validate_email (self, email):
        user = User.query.filter_by(email= email.data).first()
        if user:
            raise ValidationError('This email already exists')    

class LoginForm(FlaskForm):
    email = StringField('Email' , validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class PostForm(FlaskForm):
    title = StringField('Title' , validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
