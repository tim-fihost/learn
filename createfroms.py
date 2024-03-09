from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL

#Create a RegisterForm to register new users
class CreateRegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()]) #check if @ exists
    name = StringField("Name", validators=[DataRequired()])
    passwrod = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("SIGN ME UP")

# Create a LoginForm to login existing users
class CreateLoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")