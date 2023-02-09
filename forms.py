from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TelField,PasswordField,HiddenField,EmailField,FileField
from wtforms.validators import Email
from wtforms import validators

def length_honeypot(form,field):
   if (len(field.data)>0):
      raise validators.ValidationError('elcampo vacio')

 
class CommentForm(FlaskForm):
   username=StringField('username',[validators.length(min=4,max=25),validators.DataRequired()])
   password=PasswordField('Password',[validators.DataRequired()])
   email=EmailField('Email')
   honeypot=HiddenField('',[length_honeypot])