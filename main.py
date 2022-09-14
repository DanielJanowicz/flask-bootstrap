from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/software')
def login():
    return render_template('software.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
