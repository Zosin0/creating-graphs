from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

if __name__ == '__main__':
    app.run()
