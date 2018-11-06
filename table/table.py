from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    users = (
        {'first' : 'Michael', 'last' : 'Choi'},
        {'first' : 'John', 'last' : 'Supsupin'},
        {'first' : 'Mark', 'last' : 'Guillen'},
        {'first' : 'KB', 'last' : 'Tonel'}
    )
    return render_template("index.html", names = users)

if __name__ == "__main__":
    app.run(debug=True)