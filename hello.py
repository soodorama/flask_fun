from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return render_template("index.html", name=name)

@app.route('/repeat/<num>/<str>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def repeat(num, str):
    return str * int(num)

@app.route('/jinja2/<phrase>')
def jinja(phrase):
    return render_template("repeat.html", phrase=phrase, times=2)

if __name__ == "__main__":
    app.run(debug=True)