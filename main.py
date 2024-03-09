from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap5
from createfroms import CreateLoginForm, CreateRegisterForm
app = Flask(__name__)
app.secret_key = 'this_is_fan_based_app98783521'
Bootstrap5(app)


@app.route('/')
def home():
    return render_template("index.html")
#==================REGISTER======================
@app.route('/register', methods= ['GET','POST'])
def register():
    reg_form = CreateRegisterForm()
    if reg_form.validate_on_submit():
        return "Everything Could be fine!"
    return render_template("register.html",form=reg_form)
#====================LOGIN=======================
@app.route('/login', methods = ['GET','POST'])
def login():
    #TODO Return image on main page!
    log_form = CreateLoginForm()
    if log_form.validate_on_submit():
        return "Everything could be fine!"
    return render_template("login.html", form=log_form)
if __name__ == '__main__':
    app.run(debug=True)
    
"""My objectives with this project I want to build space and korea dev realated page!"""