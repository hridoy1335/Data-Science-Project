import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split,KFold,cross_val_score
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from src.logger import logging

logging.info('Proccess are ready to work')
df = pd.read_csv('/Users/mac/Developer/Data Science Project/data/student_performace.csv')
# df = df[['Age','Gender','Annual Income','Education Level','Location','Policy Type','Customer Feedback','Property Type','Premium Amount']]

logging.info('data are load successfull.')

df.drop_duplicates(inplace=True)

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

numerical_columns = [col for col in x.columns if x[col].dtype!="O"]
categorical_columns = [col for col in x.columns if x[col].dtype=="O"]


# numerical_columns = ['Age',
#                      'Annual Income']

# categorical_columns = ['Gender',
#                        'Location',
#                        'Property Type']


logging.info('spliting train and test.')
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


num_pipe = Pipeline(steps=[
    ('impute',SimpleImputer(strategy='median')),
    ('scaler',StandardScaler())
])

cat_pipe = Pipeline(steps=[
    ('ipute',SimpleImputer(strategy='most_frequent')),
    ('encoder',OneHotEncoder(handle_unknown='ignore',drop='first',sparse_output=False))
])


education_level_pipe = Pipeline(steps=[
    ('impute',SimpleImputer(strategy='most_frequent')),
    ('education_level_encode',OrdinalEncoder(categories=[['Secondary Education','Undergraduate','Graduate','PhD']]))
])

policy_type_pipe = Pipeline(steps=[
    ('impute',SimpleImputer(strategy='most_frequent')),
    ('policy_type_encode',OrdinalEncoder(categories=[['Basic','Comprehensive','Premium']]))
])

Customer_Feedback_pipe = Pipeline(steps=[
    ('impute',SimpleImputer(strategy='most_frequent')),
    ('Customer_Feedback_encode',OrdinalEncoder(categories=[['Poor','Average','Good']]))
])

transformer = ColumnTransformer(transformers=[
    ('num_pipe',num_pipe,numerical_columns),
    ('cat_pipe',cat_pipe,categorical_columns)
    # ('education_level_pipe',education_level_pipe,[3]),
    # ('policy_type_pipe',policy_type_pipe,[5]),
    # ('Customer_Feedback_pipe',Customer_Feedback_pipe,[6])
],remainder='passthrough',n_jobs=-1)

logging.info('transformation is going on.')

transformer.fit(x_train)

X_train = transformer.transform(x_train)
X_test = transformer.transform(x_test)

logging.info('transformation is done.')

rf = RandomForestRegressor()
# rf.fit(X_train,y_train)
# logging.info('model fit successfully.')
# y_pred = rf.predict(X_test)

# r2_s = r2_score(y_test,y_pred)
# mse = mean_squared_error(y_test,y_pred)
# mae = mean_absolute_error(y_test,y_pred)
# logging.info(f'all metrics are r2_score: {r2_s} - mean_squared_error: {mse} - mean_absolute_error: {mae}')

logging.info('cross_val_score testing')
skf = KFold(n_splits=10,shuffle=True,random_state=42)
cv_result = cross_val_score(estimator=rf,X=X_train,y=y_train,cv=skf,n_jobs=-1)
logging.info(f'cross_val_score is: {cv_result}')

print('OK')
