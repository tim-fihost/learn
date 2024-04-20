from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap5
from createfroms import CreateLoginForm, CreateRegisterForm
from video_downloader import Downloader
app = Flask(__name__)
app.secret_key = 'this_is_fan_based_app98783521'
Bootstrap5(app)

#================Index==========================
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
    log_form = CreateLoginForm()
    if log_form.validate_on_submit():
        #log_form.email.data
        return "Everything could be fine!"
   
    return render_template("login.html", form=log_form)

#==================SEARCH======================== 
#Strucre this code below!
@app.route('/search', methods=['GET','POST'])
def search():
    action = None
    if request.method == 'POST':
        path = request.form.get('path')
        print(path)
        return redirect(url_for('download'))
    return render_template("search.html")

@app.route('/download', methods=['GET','POST'])
def download():
    path = "MUST BE PASSED!"
    output = Downloader(path)
    return render_template("download.html")
if __name__ == '__main__':
    app.run(debug=True, port=8080)


