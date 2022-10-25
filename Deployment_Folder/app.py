from distutils.log import debug
from flask import Flask, request, render_template
import numpy as np
import joblib
import os
#create Flask app
app = Flask(__name__)
#run Flask app with ngrok

@app.route('/',methods = ["GET", "POST"])
def main_func():
    return render_template('index.html')
 
@app.route('/model_1',methods = ["GET", "POST"] )

#For First Year 
def model_1():
    my_prediction=[0]  

    if str(request.form)!="ImmutableMultiDict([])":
        array_1=[[
        eval(request.form.get("PH-121")),
        eval(request.form.get('HS-101')), 
        eval(request.form.get('CY-105')),  
        eval(request.form.get("HS-105/12")),      
        eval(request.form.get('MT-111')),
        eval(request.form.get('CS-105')),
        eval(request.form.get('CS-106')),
        eval(request.form.get('EL-102')),
        eval(request.form.get('EE-119')),
        eval(request.form.get('ME-107')),
        eval(request.form.get('CS-107'))]]
        loaded_rf = joblib.load("linear_regression.pkl")
        my_prediction=loaded_rf.predict(array_1)  
    return render_template('model_1.html',data=round(my_prediction[0],3))



@app.route('/model_2',methods = ["GET", "POST"] )
#For First and Second Year 
def model_2():
    my_prediction_2=[0]  

    if str(request.form)!="ImmutableMultiDict([])":
        print(request.form)
        array_2=[[
        eval(request.form.get("PH-121")),
        eval(request.form.get('HS-101')),  
        eval(request.form.get('CY-105')), 
        eval(request.form.get("HS-105/12")),
        eval(request.form.get('MT-111')),
        eval(request.form.get('CS-105')),
        eval(request.form.get('CS-106')),
        eval(request.form.get('EL-102')),
        eval(request.form.get('EE-119')),
        eval(request.form.get('ME-107')),
        eval(request.form.get('CS-107')),
        
        eval(request.form.get('HS-205/20')),   
        eval(request.form.get("MT-222")),
        eval(request.form.get('EE-222')),
        eval(request.form.get('MT-224')),
        eval(request.form.get('CS-210')),
        eval(request.form.get('CS-211')),
        eval(request.form.get('CS-203')),
        eval(request.form.get('CS-214')),
        eval(request.form.get('EE-217')),
        eval(request.form.get('CS-212')),
        eval(request.form.get('CS-215'))]]

        loaded_rf = joblib.load("RandomForestRegressor.pkl")
        my_prediction_2=loaded_rf.predict(array_2)  
    return render_template('model_2.html',data=round(my_prediction_2[0],3)) 



@app.route('/model_3',methods = ["GET", "POST"] )

#For First, Second , Third and Final Year
def model_3():
    my_prediction_3=[0]  

    if str(request.form)!="ImmutableMultiDict([])":
        array_3=[[

      
       eval(request.form.get("PH-121")),
        eval(request.form.get('HS-101')),  
        eval(request.form.get('CY-105')), 
        eval(request.form.get("HS-105/12")),   
        eval(request.form.get('MT-111')),
        eval(request.form.get('CS-105')),
        eval(request.form.get('CS-106')),
        eval(request.form.get('EL-102')),
        eval(request.form.get('EE-119')),
        eval(request.form.get('ME-107')),
        eval(request.form.get('CS-107')),
        
        eval(request.form.get('HS-205/20')),   
        eval(request.form.get("MT-222")),
        eval(request.form.get('EE-222')),
        eval(request.form.get('MT-224')),
        eval(request.form.get('CS-210')),
        eval(request.form.get('CS-211')),
        eval(request.form.get('CS-203')),
        eval(request.form.get('CS-214')),
        eval(request.form.get('EE-217')),
        eval(request.form.get('CS-212')),
        eval(request.form.get('CS-215')),

         eval(request.form.get('MT-331')),   
        eval(request.form.get("EF-303")),
        eval(request.form.get('HS-304')),
        eval(request.form.get('CS-301')),
        eval(request.form.get('CS-302')),
        eval(request.form.get('TC-383')),
        eval(request.form.get('EL-332')),
        eval(request.form.get('CS-318')),
        eval(request.form.get('CS-306')),
        eval(request.form.get('CS-312')),
        eval(request.form.get('CS-317')),

        eval(request.form.get("MT-442")),
        eval(request.form.get('CS-403')),
        eval(request.form.get('CS-421')),
        eval(request.form.get('CS-414')),
        eval(request.form.get('CS-419')),
        eval(request.form.get('CS-423')),

        ]]
        loaded_rf = joblib.load("GradientBoostingRegressor.pkl")
        my_prediction_3=loaded_rf.predict(array_3)  
    return render_template('model_3.html',data=round(my_prediction_3[0],3)) 




if __name__=="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(host="0.0.0.0",port=port,debug=False)
