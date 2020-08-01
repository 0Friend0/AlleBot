from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import DataRequired

class Items(FlaskForm):

    item = StringField('item', validators=[DataRequired()])
    price_min = StringField('price_min')
    price_max = StringField('price_max')

