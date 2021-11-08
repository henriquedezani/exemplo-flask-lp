from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', nome='Fulano')

@app.route('/bye')
def bye():
    return render_template('tchau.html')

app.run(debug=True)