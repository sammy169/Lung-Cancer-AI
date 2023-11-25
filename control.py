from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    gender = request.form.get('gender')
    age = request.form.get('age')
    return render_template('result.html', gender=gender, age=age)

if __name__ == '__main__':
    app.run(debug=True)