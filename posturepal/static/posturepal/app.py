#ignore 

from flask import Flask, render_template, request, jsonify
import math
import subprocess
import time
from threading import Lock

app = Flask(__name__)

posture_data = {
    'x': 10.0,  
    'y': 0.0,
    'z': 0.0,
    'score': 100.0
}
data_lock = Lock()

def posture_score(x, y, z):
    return 100 / (1 + (x - 10)**2 + y**2 + z**2)
 # with "ideal posture values," X will be hovering around ~10, Y and Z will be close to 0
 # with "poor posture values," X will be approaching 0, Y and Z will either increase or decrease
 # good posture values - posture score approaches 100, bad posture values - posture score approaches 0.33

def update():
    return [8, 2, 0]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        update()
        
        with data_lock:
            x = posture_data['x']
            y = posture_data['y']
            z = posture_data['z']
            posture_data['score'] = round(posture_score(x, y, z), 2)
        
        return jsonify(posture_data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/posture-stream')
def posture_stream():
    def generate():
        while True:
            with data_lock:
                current_data = posture_data.copy()
            yield f"data: {current_data}\n\n"
            time.sleep(0.1)
    
    return Response(generate(), mimetype='text/event-stream')

@app.route('/run-graph', methods=['POST'])
def run_graph():
    try:
        subprocess.Popen(['python', 'graph.py'])
        return jsonify({'status': 'Graph launched successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
