from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LogisticRegression


app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')


def create_model():
    df = pd.read_csv("data/survey_lung_cancer.csv")
    
    gender_mapping = {'M': 0, 'F': 1}
    df['GENDER'] = df['GENDER'].map(gender_mapping)

    result_mapping = {'YES': 1, 'NO': 0}
    df['LUNG_CANCER'] = df['LUNG_CANCER'].map(result_mapping)
    
    X = df.iloc[:, :-1]  # Select all columns except the last one
    y = df.iloc[:, -1]  # Select the last column as the target variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # creating the logistic regression model
    model = LogisticRegression()

    # fitting the model to the training data
    model.fit(X_train,y_train)

    return model, X.columns

def predict(attributes):

    model, columns = create_model()

    user_entry_df = pd.DataFrame([attributes], columns=columns)

    # Predicting the target variable for the test data
    predicted_value = model.predict(user_entry_df)

    return predicted_value[0]

@app.route('/result', methods=['POST'])
def result():

    gender = request.form.get('gender')
    age = request.form.get('age')
    smoking = request.form.get('smoking')
    yf = request.form.get('yf')
    anxiety = request.form.get('anxiety')
    peerpressure = request.form.get('peerpressure')
    chronicdisease = request.form.get('chronicdisease')
    fatigue = request.form.get('fatigue')
    allergy = request.form.get('allergy')
    wheezing = request.form.get('wheezing')
    alcohol = request.form.get('alcohol')
    cough = request.form.get('cough')
    shortbreath = request.form.get('shortbreath')
    swallowdiff = request.form.get('swallowdiff')
    chestpain = request.form.get('chestpain')

    print([gender, age, smoking, yf, anxiety, 
                            peerpressure, chronicdisease, fatigue, allergy, wheezing, 
                            alcohol, cough, shortbreath, swallowdiff, chestpain])

    predicted_value = predict([gender, age, smoking, yf, anxiety, 
                            peerpressure, chronicdisease, fatigue, allergy, wheezing, 
                            alcohol, cough, shortbreath, swallowdiff, chestpain])
    
    print(predicted_value)

    if predicted_value == 1:
        predicted_value = "You have a high chance of getting lung cancer."
    else:
        predicted_value = "You have a low chance of getting lung cancer."
     
    return render_template('result.html',
        gender=gender, 
        age=age, 
        smoking=smoking,
        yf=yf,
        anxiety=anxiety,
        peerpressure=peerpressure,
        chronicdisease=chronicdisease,
        fatigue=fatigue,
        allergy=allergy,
        wheezing=wheezing,
        alcohol=alcohol,
        cough=cough,
        shortbreath=shortbreath,
        swallowdiff=swallowdiff,
        chestpain=chestpain, 
        predicted_value=predicted_value)

if __name__ == '__main__':
    app.run(debug=True)