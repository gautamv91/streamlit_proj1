import streamlit as st
import joblib

st.title("Insurance premium prediction tool")

# Defining the encodings
encoding_dict = {'age_grp': {'18-30':1, '31-50':2, '50+':3},
                 'sex': {'male':1, 'female':2},
                 'smoker': {'no':1,'yes':2},
                 'region': {'southwest':1, 'southeast':2, 'northwest':3, 'northeast':4}
                 }

model = joblib.load("./models/insurance-model.joblib")


st.subheader("Fill the details below to get a prediction:")

col1, col2 = st.columns(2)


age = col1.selectbox("Age group", options=list(encoding_dict['age_grp'].keys()))
sex = col1.radio("Gender", options=list(encoding_dict['sex'].keys()))
region = col2.selectbox("Region", options=list(encoding_dict['region'].keys()))
smoker = col2.radio("Is smoker?", options=list(encoding_dict['smoker'].keys()))
children = col1.slider("Number of children", min_value=0, max_value=5, value=0, step=1)
bmi = col2.number_input("BMI", min_value=15.0, max_value=55.0, value=20.0, step=0.5)

def model_pred(children, age, sex, smoker, region, bmi):
    
    # Convert categorical features back to numeric values
    age_enc = encoding_dict['age_grp'][age]
    sex_enc = encoding_dict['sex'][sex]
    smoker_enc = encoding_dict['smoker'][smoker]
    region_enc = encoding_dict['region'][region]
    
    # Ensure numeric data is float or int as required
    data=[[age_enc,sex_enc,smoker_enc,region_enc,float(bmi),int(children)]]
    
    prediction = model.predict(data)
    return round(prediction[0],2)


if st.button("Predict"):
   premium =  model_pred(children, age, sex, smoker, region, bmi)
   st.write(f"**Predicted insurance premium amount: {premium}**")
else:
    st.write("Click the **Predict** button after entering all the details.")