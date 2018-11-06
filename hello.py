from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return "Hi " + name + "!"

@app.route('/repeat/<num>/<str>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def repeat(num, str):
    return str * int(num)

if __name__ == "__main__":
    app.run(debug=True)