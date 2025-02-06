from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kontakt')
def contact():
    return render_template('contact.html')

@app.route('/o-nas')
def about():
    return render_template('about.html')

# @app.route('/uslugi')
# def services():
#     return render_template('index.html')

@app.route('/uslugi/naprawa')
def fix():
    return render_template('fix.html')

@app.route('/uslugi/komis')
def dealership():
    return render_template('dealership.html')

@app.route('/uslugi/czesci')
def parts():
    return render_template('parts.html')

@app.route('/uslugi/detailing')
def detailing():
    return render_template('detailing.html')

if __name__ == "__main__":
    app.run()