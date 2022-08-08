from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TestForm(FlaskForm):
    name = StringField('Insert your Name', validators=[DataRequired()])
    submit = SubmitField('Submit')