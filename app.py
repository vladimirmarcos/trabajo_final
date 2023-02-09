#---------------------------------importes------------------------------------------------------------
from flask import Flask,render_template,request
import forms

#-----------------------------------------------------------------------------------------------------


#---------------------------------configuracion-------------------------------------------------------
app=Flask(__name__)




#-----------------------------------------------------------------------------------------------------




#---------------------------------rutas---------------------------------------------------------------
@app.route('/')
def index():
    return render_template ('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
    login_form=forms.CommentForm(request.form)  
    return render_template('login.html',form=login_form)

@app.route('/registro',methods=['GET','POST'])
def registro():
      registro_form=forms.CommentForm(request.form)  
      return render_template('registro.html',form=registro_form)

#-----------------------------------------------------------------------------------------------------


if __name__== '__main__':
    app.run(debug=True)