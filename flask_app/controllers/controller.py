from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model import Email

@app.route('/')
def home():

    return render_template('index.html')



@app.route('/process',methods=['POST'])
def process():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.save(request.form)
    email=Email.get_one(request.form)

    flash(f'successfully added {email} to  email database! ')
    return redirect('/results')



@app.route('/results')
def results():

    
    
    return render_template("success.html",emails=Email.get_all())



@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect('/results')