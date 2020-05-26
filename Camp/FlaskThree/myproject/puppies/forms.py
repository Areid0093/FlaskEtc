from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    
    name = StringField('Name of puppy: ')
    submit = SubmitField('Add Puppy')
    
class DelForm(FlaskForm):
    
    id = IntegerField('ID number of puppy: ')
    submit = SubmitField('Remove Puppy')