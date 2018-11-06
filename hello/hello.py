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

@app.route('/repeat/<num>/<str>')
def repeat(num, str):
    return str * int(num)

@app.route('/jinja2/<phrase>')
def jinja(phrase):
    student_info = (
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    )
    return render_template("repeat.html", phrase=phrase, times=2, students=student_info)

if __name__ == "__main__":
    app.run(debug=True)