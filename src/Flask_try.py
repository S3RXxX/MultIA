from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def do_all():
    print("Hello from the other side")

if __name__=="__main__":
    app.run(debug=True)