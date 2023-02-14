#---------------------------------importes------------------------------------------------------------
from flask import Flask,render_template,request
from flask_wtf import CSRFProtect,FlaskForm
import forms
from wtforms import FileField
import os
from werkzeug.utils import secure_filename
#-----------------------------------------------------------------------------------------------------


#---------------------------------configuracion-------------------------------------------------------
app=Flask(__name__)
app.secret_key='kjasdkjasd_ASDASD'
csrf=CSRFProtect(app)
app.config["UPLOAD_FOLDER"]="static/uploads"
from funcionesvarias import allowed_file,ALLOWED_EXTENSIONS,red

class MyForm (FlaskForm):
      image =FileField('image')



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


@app.route('/upload',methods=['GET','POST'])
def upload ():
    form=MyForm(request.form)
    if form.validate_on_submit():
        
        file=request.files["image"]
        filename= secure_filename(file.filename)
        if file and allowed_file(filename):
            file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
            img_modelo= os.path.join(app.config["UPLOAD_FOLDER"],filename)
            predictions_raw=red(img_modelo)
            return render_template ('mostrar_usuarios.html',mensaje1=predictions_raw[0,0],mensaje2=predictions_raw[0,1],mensaje3=predictions_raw[0,2])
        else:
         return render_template ('mostrar_usuarios.html',mensaje="algo paso ")
    return render_template('upload.html',form=form)   





#-----------------------------------------------------------------------------------------------------


if __name__== '__main__':
    app.run(debug=True)