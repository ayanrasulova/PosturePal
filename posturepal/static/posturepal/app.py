from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def posture_score(x, y, z):
    return 100 / (1 + (x - 10)**2 + y**2 + z**2) 
    # with "ideal posture values," X will be hovering around ~10, Y and Z will be close to 0
    # with "poor posture values," X will be approaching 0, Y and Z will either increase or decrease 
    # good posture values - posture score approaches 100, bad posture values - posture score approaches 0.33

@app.route('/')
def index(): return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json() # takes in input
        score = posture_score(
            float(data['x']),
            float(data['y']),
            float(data['z'])
        )
        return jsonify({'score': round(score, 2)}) # rounds to 2 decimal places
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

# if cant resolve importing flask, use diff python interpreter with updated version!