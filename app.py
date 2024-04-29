# Import libraries
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the model
diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('saved_models/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('saved_models/parkinsons_model.sav','rb'))
kidney_model = pickle.load(open('saved_models/kidney_disease_model.sav','rb'))


@app.route('/home', methods=['GET', 'POST'])
def indexnew():
    return render_template('home.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def predict():
    # Extract data from the form
    name = request.form['name']
    email = request.form['email']
    Pregnancies = request.form['Pregnancies']
    Glucose = request.form['Glucose']
    BloodPressure = request.form['BloodPressure']
    SkinThickness = request.form['SkinThickness']
    Insulin = request.form['Insulin']
    BMI = request.form['BMI']
    DiabetesPedigreeFunction = request.form['DiabetesPedigreeFunction']
    Age = request.form['Age']

    # Handle empty fields
    if not Pregnancies:
        Pregnancies = 0
    if not Glucose:
        Glucose = 0
    if not BloodPressure:
        BloodPressure = 0
    if not SkinThickness:
        SkinThickness = 0
    if not Insulin:
        Insulin = 0
    if not BMI:
        BMI = 0
    if not DiabetesPedigreeFunction:
        DiabetesPedigreeFunction = 0
    if not Age:
        Age = 0

    # Convert features to appropriate data types
    features = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]

    # Make prediction
    prediction = diabetes_model.predict([features])[0]

    # Interpret prediction
    result = "Diabetic" if prediction == 1 else "Not Diabetic"

    # Prepare response data
    input_data = {
        "Number of Pregnancies": Pregnancies,
        "Glucose Level": Glucose,
        "Blood Pressure": BloodPressure,
        "Skin Thickness": SkinThickness,
        "Insulin Level": Insulin,
        "BMI": BMI,
        "Diabetes Pedigree Function": DiabetesPedigreeFunction,
        "Age": Age
    }

    # PackAge data to be sent to result.html
    response = {
        "personal_info": [name, email],
        "input_data": input_data,
        "result": result
    }

    return render_template("result.html", result=response)

@app.route('/heart', methods=['GET', 'POST'])
def heart():
    return render_template('heart.html')

@app.route('/api1', methods=[ 'POST'])
def predict_heart_disease():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    sex = request.form['sex']
    cp = request.form['cp']
    trestbps = request.form['trestbps']
    chol = request.form['chol']
    fbs = request.form['fbs']
    restecg = request.form['restecg']
    thalach = request.form['thalach']
    exang = request.form['exang']
    oldpeak = request.form['oldpeak']
    slope = request.form['slope']
    ca = request.form['ca']
    thal = request.form['thal']

    features = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
    prediction = heart_model.predict([features])[0]
    result = "You may have Heart Disease" if prediction == 1 else "You don't have heart Disease"
    input_data = {"Age": [age],
                              "Sex": [sex],
                              "Chest Pain types": [cp],
                               "Resting Blood Pressure": [trestbps],
                               "Serum Cholestoral in mg/dl": [chol],
                               "Fasting Blood Sugar > 120 mg/dl": [fbs],
                               "Resting Electrocardiographic results": [restecg],
                               "Maximum Heart Rate achieved": [thalach],
                               "Exercise Induced Angina": [exang],
                               "ST depression induced by exercise": [oldpeak],
                               "Slope of the peak exercise ST segment": [slope],
                               "Major vessels colored by flourosopy": [ca],
                               "Thal": [thal]
                               }

    response = {
        "personal_info": [name, email],
        "input_data": input_data,
        "result": result
    }

    return render_template("result1.html", result=response)

@app.route('/parkinsons', methods=['GET', 'POST'])
def parkinson():
    return render_template('parkinsons.html')

@app.route('/api2', methods=[ 'POST'])
def predict_parkinsons_disease():
    name = request.form['name']
    email = request.form['email']
    fo = request.form['fo']
    fhi = request.form['fhi']
    flo = request.form['flo']
    Jitter_percent = request.form['Jitter_percent']
    Jitter_Abs = request.form['Jitter_Abs']
    RAP = request.form['RAP']
    PPQ = request.form['PPQ']
    DDP = request.form['DDP']
    Shimmer = request.form['Shimmer']
    Shimmer_dB = request.form['Shimmer_dB']
    APQ3 = request.form['APQ3']
    APQ5 = request.form['APQ5']
    APQ = request.form['APQ']
    DDA = request.form['DDA']
    NHR = request.form['NHR']
    HNR = request.form['HNR']
    RPDE = request.form['RPDE']
    DFA = request.form['DFA']
    spread1 = request.form['spread1']
    spread2 = request.form['spread2']
    D2 = request.form['D2']
    PPE = request.form['PPE']


    features = [float(fo),float(fhi), float(flo), float(Jitter_percent), 
                float(Jitter_Abs), float(RAP), float(PPQ), 
                float(DDP), float(Shimmer), float(Shimmer_dB), 
                float(APQ3), float(APQ5), float(APQ), float(DDA), 
                float(NHR), float(HNR), float(RPDE), 
                float(DFA), float(spread1), float(spread2), float(D2), 
                float(PPE)]
    prediction = parkinsons_model.predict([features])[0]
    result = "You may have Parkinsons Disease" if prediction == 1 else "You don't have Parkinsons Disease"
    input_data = {'MDVP:Fo(Hz)': [fo],
                                          'MDVP:Fhi(Hz)': [fhi],
                                          'MDVP:Flo(Hz)': [flo],
                                          'MDVP:Jitter(%)': [Jitter_percent],
                                          'MDVP:Jitter(Abs)': [Jitter_Abs],
                                          'MDVP:RAP': [RAP],
                                          'MDVP:PPQ': [PPQ],
                                          'Jitter:DDP': [DDP],
                                          'MDVP:Shimmer': [Shimmer],
                                          'MDVP:Shimmer(dB)': [Shimmer_dB],
                                          'Shimmer:APQ3': [APQ3],
                                          'Shimmer:APQ5': [APQ5],
                                          'MDVP:APQ': [APQ],
                                          'Shimmer:DDA': [DDA],
                                          'NHR': [NHR],
                                          'HNR': [HNR],
                                          'RPDE': [RPDE],
                                          'DFA': [DFA],
                                          'spread1': [spread1],
                                          'spread2': [spread2],
                                          'D2': [D2],
                                          'PPE': [PPE]
                               }

    response = {
        "personal_info": [name, email],
        "input_data": input_data,
        "result": result
    }

    return render_template("result2.html", result=response)




@app.route('/kidney', methods=['GET', 'POST'])
def kidney():
    return render_template('kidney.html')

@app.route('/api3', methods=[ 'POST'])
def predict_kidney_disease():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    blood_pressure = request.form['blood_pressure']
    specific_gravity = request.form['specific_gravity']
    albumin = request.form['albumin']
    sugar = request.form['sugar']
    red_blood_cells = request.form['red_blood_cells']
    pus_cell = request.form['pus_cell']
    pus_cell_clumps = request.form['pus_cell_clumps']
    bacteria = request.form['bacteria']
    blood_glucose_random = request.form['blood_glucose_random']
    blood_urea = request.form['blood_urea']
    serum_creatinine = request.form['serum_creatinine']
    sodium = request.form['sodium']
    potassium = request.form['potassium']
    haemoglobin = request.form['haemoglobin']
    packed_cell_volume = request.form['packed_cell_volume']
    white_blood_cell_count = request.form['white_blood_cell_count']
    red_blood_cell_count = request.form['red_blood_cell_count']
    hypertension = request.form['hypertension']
    diabetes_mellitus = request.form['diabetes_mellitus']
    coronary_artery_disease = request.form['coronary_artery_disease']
    appetite = request.form['appetite']
    peda_edema = request.form['peda_edema']
    aanemia = request.form['aanemia']



    
    features = [float(age), float(blood_pressure), float(specific_gravity), float(albumin), 
            float(sugar), float(red_blood_cells), float(pus_cell), 
            float(pus_cell_clumps), float(bacteria), float(blood_glucose_random), 
            float(blood_urea), float(serum_creatinine), float(sodium), 
            float(potassium), float(haemoglobin), float(packed_cell_volume), 
            float(white_blood_cell_count), float(red_blood_cell_count), 
            float(hypertension), float(diabetes_mellitus), float(coronary_artery_disease), 
            float(appetite), float(peda_edema), float(aanemia)]

    prediction = kidney_model.predict([features])[0]
    result = "You may have Kidney Disease" if prediction == 1 else "You don't have Kidney Disease"
    input_data = { 'Age (in years)': [age],
              'Blood Pressure (in mm/Hg)': [blood_pressure],
              'Specific Gravity': [specific_gravity],
              'Albumin (0, 1, 2, 3, 4, 5)': [albumin],
              'Sugar (0, 1, 2, 3, 4, 5)': [sugar],
              'Red Blood Cells (0: Abnormal; 1: Normal)': [red_blood_cells],
              'Pus Cell (0: Abnormal; 1: Normal)': [pus_cell],
              'Pus Cell Clumps (0: Not Present; 1: Present)': [pus_cell_clumps],
              'Bacteria (0: Not Present; 1: Present)': [bacteria],
              'Blood Glucose Random (in mgs/dl)': [blood_glucose_random],
              'Blood Urea (in mgs/dl)': [blood_urea],
              'Serum Creatinine (in mgs/dl)': [serum_creatinine],
              'Sodium (in mEq/L)': [sodium],
              'Potassium (in mEq/L)': [potassium],
              'Haemoglobin (in gms)': [haemoglobin],
              'Packed Cell Volume': [packed_cell_volume],
              'White Blood Cell Count (in cells/cumm)': [white_blood_cell_count],
              'Red Blood Cell Count (in millions/cmm)': [red_blood_cell_count],
              'Hypertension (0: No; 1: Yes)': [hypertension],
              'Diabetes Mellitus (0: No; 1: Yes)': [diabetes_mellitus],
              'Coronary Artery Disease (0: No; 1: Yes)': [coronary_artery_disease],
              'Appetite (0: Good; 1: Poor)': [appetite],
              'Pedal Edema (0: No; 1: Yes)': [peda_edema],
              'Anemia (0: No; 1: Yes)': [aanemia]
                               }

    response = {
        "personal_info": [name, email],
        "input_data": input_data,
        "result": result
    }

    return render_template("result3.html", result=response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
