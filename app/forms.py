from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class RegisterForm(FlaskForm):
  firstname = StringField('firstname', validators=[InputRequired()])
  lastname = StringField('lastname', validators=[InputRequired()])
  email = StringField('email', validators=[InputRequired()])
  location = StringField('location', validators=[InputRequired()])
  
  gender = SelectField('gender', choices=[('M','Male'), ('F','Female')], 
                                 validators=[InputRequired()])
  
  biography = TextAreaField('biography', validators=[InputRequired()])
  
  photo = FileField('photo', validators=[
    FileRequired(),
    FileAllowed(['jpg', 'png', 'Images only!'])
  ])