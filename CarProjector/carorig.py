from flask import Flask , render_template, request, redirect, url_for
import pandas as pd
import numpy as np
app = Flask(__name__)
car=pd.read_csv('Cleaned_Car_data.csv')
@app.route('/')
def index():
    companies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    year=sorted(car['year'].unique())
    fuel_type=car['fuel_type'].unique()
    return render_template('index.html',companies=companies,car_models=car_models,year=year,fuel_type=fuel_type)
@app.route('/predict',methods=['GET','POST'])
def predict():
    company=request.form.get('company')
    year=request.form.get('year')
    fuel_type=request.form.get('fuel_type')
    car_model=request.form.get('car Model')
    year=int(request.form.get('year'))
    kms_driven=(request.form.get('kms_driven'))

    print(company,car_model,year,fuel_type,kms_driven)

    prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                            data=np.array([car_model, company, year, kms_driven, fuel_type]).reshape(1, 5)))
    print(prediction)
    return str(np.round(prediction[0], 2))


if __name__ == '__main__':
    app.run(debug=True)

