from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class RegForm(FlaskForm):
    username = StringField('Insert your Username', validators=[DataRequired()])
    name = StringField('Insert your Name', validators=[DataRequired()])
    email = StringField('Insert your Email', validators=[DataRequired(), Email()])
    password = PasswordField('Insert your Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')