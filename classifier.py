import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error





train_df = pd.read_csv("./train.csv")
test_df = pd.read_csv("./test.csv")


oldsurvivor = train_df.loc[(train_df["Age"] > 60) & (train_df["Survived"] == 1)]

print oldsurvivor




# print train_df
# pred_df = pd.DataFrame(y_pred, index=test_df["Id"], columns=["SalePrice"])
# pred_df.to_csv('output.csv', header=True, index_label='Id')
