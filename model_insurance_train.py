### Basic model for deployment on Streamlit

import pandas as pd
import numpy as np
import os
from sklearn.tree import DecisionTreeRegressor
import joblib as jl

os.chdir("C:\D_Drive\Python\github_publish\model_building")
from model_building.eda_utils.eda import EDA

raw_data = pd.read_csv("C:/D_Drive/Python/MLOps projects/streamlit/streamlit_proj1/datasets/insurance.csv")

eda_class = EDA()
data_analyze = raw_data.copy(deep=True)
data_summary = eda_class.create_data_summary(data_analyze)

data_analyze['age_grp'] = np.where(data_analyze['age']<=30,'18-30', np.where(data_analyze['age']>50,'50+','31-50'))

num_cols = ['bmi','children']
cat_cols = ['age_grp','sex','smoker','region']
y = 'charges'

X = data_analyze[['age_grp','sex','smoker','region','bmi','children']]

encoding_dict = {'age_grp': {'18-30':1, '31-50':2, '50+':3},
                 'sex': {'male':1, 'female':2},
                 'smoker': {'no':1,'yes':2},
                 'region': {'southwest':1, 'southeast':2, 'northwest':3, 'northeast':4}
                 }

X.replace(encoding_dict, inplace=True)

model = DecisionTreeRegressor()

model.fit(X,data_analyze[y])

# dump model using joblib
# jl.dump(model, "C:/D_Drive/Python/MLOps projects/streamlit/streamlit_proj1/models/insurance-model.pkl")
jl.dump(model, "C:/D_Drive/Python/MLOps projects/streamlit/streamlit_proj1/models/insurance-model.joblib")
