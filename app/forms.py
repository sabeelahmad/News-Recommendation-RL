from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NewsQueryForm(FlaskForm):
  search_query = StringField('Search For News', validators=[DataRequired()])
  submit = SubmitField('Go!') 

