from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create():
    info = {
        'name': request.form['name'],
        'location': request.form['loc'],
        'language': request.form['lang'],
        'comment': request.form['comment']
    }
    return render_template("result.html", info=info)

if __name__ == "__main__":
    app.run(debug=True)