from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    vitals = {
        "blood_pressure": "120/80 mmHg",
        "glucose_level": "90 mg/dL",
        "heart_rate": "72 bpm",
        "weight": "70 kg"
    }
    return render_template('dashboard.html', vitals=vitals)

if __name__ == '__main__':
    app.run(debug=True)
