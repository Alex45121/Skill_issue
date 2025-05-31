import pandas as pd 
import numpy as np


# For splitting data into training and testing sets
from sklearn.model_selection import train_test_split

# For the regression models
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.neighbors import KNeighborsRegressor

# For evaluating the models
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("D:\\Python projects\\Data_Science\\Data_test_project\\WA_Fn-UseC_-Telco-Customer-Churn.csv")

s1 = ['InternetService', 'Contract']

Num_conv = pd.get_dummies(df[s1],dtype= int)

X = pd.concat([df['tenure'], Num_conv], axis=1)

y = df["MonthlyCharges"]

"""model = LinearRegression()

x_train, x_test, y_train, y_test = train_test_split(X,y, train_size = 0.2, random_state = 66 )

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(x_train,y_pred)"""

print(X.shape, y.shape)