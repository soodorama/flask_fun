from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create():
    name = request.form['name']
    email = request.form['email']
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)