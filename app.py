from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Page/index.html")

#@app.route("/austria")
#def austria():
#    return render_template("Page/austria.html")
