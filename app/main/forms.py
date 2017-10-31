from flask_wtf import FlaskForm
from wtforms import SelectField,StringField,SubmitField,TextAreaField
from wtforms.validators import Required
from ..models import Category

class NewPitch(FlaskForm):
    choic = [('business', 'business'),('science', 'science'),('tech', 'tech'),('interview', 'interview')]
    title=StringField('Pitch Title',validators=[Required()])
    category=SelectField('Categories',choices = choic)
        # language = SelectField('Languages', choices = [('cpp', 'C++'),('py', 'Python')])
    body=TextAreaField('The Idea',validators=[Required()])
    submit=SubmitField('Submit')
