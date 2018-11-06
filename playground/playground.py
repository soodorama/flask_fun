from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html", boxes = 3, color="blue")

@app.route('/play/<num>')
def playx(num):
    return render_template("index.html", boxes = int(num), color="blue")
    
@app.route('/play/<num>/<col>')
def playxy(num, col):
    return render_template("index.html", boxes = int(num), color=col)

if __name__ == "__main__":
    app.run(debug=True)