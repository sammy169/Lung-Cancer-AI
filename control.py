from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

# yf stands for yellow_fingers

@app.route('/result', methods=['POST'])
def result():

    gender = request.form.get('gender')
    age = request.form.get('age')
    smoking = request.form.get('smoking')
    yf = request.form.get('yf')
    anxiety = request.form.get('anxiety')
    peerpressure = request.form.get('peerpressure')
    chronicdisease = request.form.get('chronicdisease')

    return render_template('result.html',
        gender=gender, 
        age=age, 
        smoking=smoking,
        yf=yf,
        anxiety=anxiety,
        peerpressure=peerpressure,
        chronicdisease=chronicdisease,)

if __name__ == '__main__':
    app.run(debug=True)