# data prep and ml with multiple imputation - google colab
# by RWD_JBL

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np

data = pd.read_csv('/PATH/FILE.csv')
data.isnull().sum() # Check Missing Values

!pip install impyute
from impyute.imputation.cs import mice # MICE: Multiple Imputation by Chained Equations
imputed_training = mice(X.values)
type(imputed_training) # numpy.ndarray

X_2 = pd.DataFrame(imputed_training, columns=['COLUMN_1', 'COLUMN_2', 'COLUMN_3']) # X -> X_2
X_2.isnull().sum() # Missing Values: 0
type(X_2) # pandas.core.frame.DataFrame

from sklearn.model_selection import train_test_split, GridSearchCV
X_train, X_test, y_train, y_test = train_test_split(X_2, y, test_size=0.25, random_state=42)

# Standardization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_test)
type(scaler.fit(X_test))
X_scaled = scaler.transform(X_test)
X_test = pd.DataFrame(X_scaled, columns=['AGE_BLOOD', 'SEX','EXERCI_FREQ_RSPS_CD','HEIGHT','WEIGHT',
                                         'BMI','WAIST','BP_HIGH','BP_LWST','TOT_CHOLE',
                                         'LDL_CHOLE','HDL_CHOLE','TRIGLYCERIDE','BLDS','SGOT_AST',
                                         'SGPT_ALT','GAMMA_STP','CREATINE','TM1_DRKQTY_RSPS_CD','DRINK_HABIT_RSPS_CD',
                                         'DSQTY_RSPS_CD','SMK_STAT_TYPE_RSPS_CD'])

# Normalization
from sklearn.preprocessing import MinMaxScaler
scaler = StandardScaler()
scaler.fit(X_test)
type(scaler.fit(X_test))
X_scaled = scaler.transform(X_test)
X_test = pd.DataFrame(X_scaled, columns=['AGE_BLOOD', 'SEX','EXERCI_FREQ_RSPS_CD','HEIGHT','WEIGHT',
                                         'BMI','WAIST','BP_HIGH','BP_LWST','TOT_CHOLE',
                                         'LDL_CHOLE','HDL_CHOLE','TRIGLYCERIDE','BLDS','SGOT_AST',
                                         'SGPT_ALT','GAMMA_STP','CREATINE','TM1_DRKQTY_RSPS_CD','DRINK_HABIT_RSPS_CD',
                                         'DSQTY_RSPS_CD','SMK_STAT_TYPE_RSPS_CD'])

from sklearn.metrics import accuracy_score, r2_score, f1_score, auc, roc_auc_score, roc_curve, mean_squared_error as MSE
from sklearn.metrics import precision_score, recall_score, confusion_matrix

from xgboost import XGBClassifier
import xgboost as xgb

model = XGBClassifier()

#

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

model_lr = LogisticRegression().fit(X_train, y_train)
probs_lr = model_lr.predict_proba(X_test)[:, 1]

model_dt = DecisionTreeClassifier().fit(X_train, y_train)
probs_dt = model_dt.predict_proba(X_test)[:, 1]

model_rf = RandomForestClassifier().fit(X_train, y_train)
probs_rf = model_rf.predict_proba(X_test)[:, 1]

model_xg = XGBClassifier().fit(X_train, y_train)
probs_xg = model_xg.predict_proba(X_test)[:, 1]

#

auc_lr = roc_auc_score(y_test, probs_lr)
fpr_lr, tpr_lr, thresholds_lr = roc_curve(y_test, probs_lr)

auc_dt = roc_auc_score(y_test, probs_dt)
fpr_dt, tpr_dt, thresholds_dt = roc_curve(y_test, probs_dt)

auc_rf = roc_auc_score(y_test, probs_rf)
fpr_rf, tpr_rf, thresholds_rf = roc_curve(y_test, probs_rf)

auc_xg = roc_auc_score(y_test, probs_xg)
fpr_xg, tpr_xg, thresholds_xg = roc_curve(y_test, probs_xg)

print("AUC_LR: %.4f" % auc_lr)
print("AUC_DT: %.4f" % auc_dt)
print("AUC_RF: %.4f" % auc_rf)
print("AUC_XG: %.4f" % auc_xg)

#

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 7))
plt.plot(fpr_lr, tpr_lr, label=f'AUC (Logistic Regression) = {auc_lr:.2f}')
plt.plot(fpr_dt, tpr_dt, label=f'AUC (Decision Tree) = {auc_dt:.2f}')
plt.plot(fpr_rf, tpr_rf, label=f'AUC (Random Forests) = {auc_rf:.2f}')
plt.plot(fpr_xg, tpr_xg, label=f'AUC (XGBoost) = {auc_xg:.2f}')
plt.plot([0, 1], [0, 1], color='blue', linestyle='--', label='Baseline')
plt.title('ROC Curve', size=20)
plt.xlabel('False Positive Rate', size=14)
plt.ylabel('True Positive Rate', size=14)
plt.legend()

#

xgb.plot_importance(model_xg)

# Do GridSearchCV for Optimization ?
grid_parameters = {"max_depth": [10, 15, 20, 22],
                   "min_samples_split": [2, 3]}
grid_model = GridSearchCV(model, param_grid=grid_parameters, cv=5, refit=True)
grid_model.fit(X_train, y_train.values.ravel())

#

grid_model.fit(X_train, y_train.values.ravel())

print("Best Estimator found: ", grid_model.best_estimator_)
print("Best Score found: ", grid_model.best_score_)
print("Best Parameters found: ", grid_model.best_params_)
print("Lowest RMSE found: ", np.sqrt(np.abs(grid_model.best_score_)))

#

scores_df = pd.DataFrame(grid_model.cv_results_)
scores_df

#

model2 = XGBClassifier(max_depth='22')
model_xg2 = model2.fit(X_train, y_train, eval_metric='auc')
probs_xg2 = model_xg.predict_proba(X_test)[:, 1]
y_pred2 = model2.predict(X_test)

accuracy = accuracy_score(y_test, y_pred2)
roc = roc_auc_score(y_test,y_pred2)
print("Accuracy: %.4f%% " % (accuracy * 100))
print("AUC: %.4f%% " % (roc * 100))
