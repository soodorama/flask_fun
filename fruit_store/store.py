from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout')
def checkout():
    info = {
        
    }
    return render_template("checkout.html")

if __name__ == "__main__":
    app.run(debug=True)