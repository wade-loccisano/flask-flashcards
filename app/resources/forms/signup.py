from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class SignUpForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=50)]
    )
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    recaptcha = RecaptchaField()
