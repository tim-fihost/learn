from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
    
"""My objectives with this project I want to build space and korea dev realated page!"""