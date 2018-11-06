from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html", boxes = 3)

@app.route('/play/<num>')
def playx(num):
    return render_template("index.html", boxes = int(num))

if __name__ == "__main__":
    app.run(debug=True)