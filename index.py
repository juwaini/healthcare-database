from flask import Flask 
from flask import jsonify 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    panels = (
            {'text': 'Patients', 'href': 'patients'},
            {'text': 'Doctors', 'href': 'doctors'},
            {'text': 'Hospitals', 'href': 'hospitals'},
            {'text': 'Diagnosises', 'href': 'diagnosises'},
            )
    return render_template('index.html', panels=panels)

@app.route('/api/patients/', methods=["GET"])
def patients():
    value = {'name': 'Ahmad Albab.'}
    return jsonify(value)

@app.route('/api/hospitals/', methods=["GET"])
def hospitals():
    value = {'name': 'Hospital Shah Alam'}
    return jsonify(value)

if __name__ == '__main__':
    app.run()
