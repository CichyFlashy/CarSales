from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kontakt')
def contact():
    return '<h1>Kontakt</h1>'

@app.route('/o-nas')
def about():
    return '<h1>O nas</h1>'

@app.route('/uslugi')
def services():
    return '<h1>Usługi</h1>'

@app.route('/uslugi/naprawa')
def fix():
    return '<h1>Naprawa</h1>'

@app.route('/uslugi/komis')
def dealership():
    return '<h1>Komis</h1>'

@app.route('/uslugi/czesci')
def parts():
    return '<h1>Części samochodowe</h1>'

@app.route('/uslugi/detailing')
def detailing():
    return '<h1>Detailing</h1>'

if __name__ == "__main__":
    app.run()