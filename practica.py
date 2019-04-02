import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix, f1_score, recall_score, precision_score


def dummy_format(data, cat_var_name):
    _data = data.copy(deep=True)
    dummy = _data.pop(cat_var_name)
    dummies = pd.get_dummies(dummy, columns=[cat_var_name], drop_first=True)
    return pd.concat([_data, dummies], axis=1)

#1.-lectura de datos con  codificacion  cp1252 para utf-8
data  = pd.read_csv('C:/Users/BRM00000/Desktop/LGG_MRP_DEMOGRAFICAS_BADRATE_2.csv',encoding='cp1252')

# 2.-Limpieza y manipulacion de datos .
data = data[(data['GENERO']=='FEMENINO') | (data['GENERO']=='MASCULINO')]
new_data = dummy_format(data, 'GENERO')
new_data = dummy_format(new_data, 'ESTADO_CIVIL')
data_bu = data.copy(deep=True)
print(data)
c1  = data[['GENERO']]
print(c1)
cl = pd.get_dummies(c1, columns = ["GENERO"], drop_first = True)
print(c1)

new_data2 = new_data[(new_data['BMI']=='BUENO') | (new_data['BMI']=='MALO')]
print(new_data2)

new_data2 = dummy_format(new_data2, 'BMI')
print(new_data2)

datar  = new_data2[['MALO','NO_DEPENDIENTES','ANT_DOM_MESES','ANT_EMP_MESES'
               ,'MASCULINO','Casado(a) Sociedad Conyugal','Divorciado(a)','Soltero(a)',
                    'Unión Libre','Viudo(a)']]

datar.loc[datar['NO_DEPENDIENTES'] == 'Más de 6', 'NO_DEPENDIENTES'] = 20

datar['NO_DEPENDIENTES'].replace(['Más de 6'], 20)
print(datar)



bmi_X_train = datar[['NO_DEPENDIENTES','ANT_DOM_MESES','ANT_EMP_MESES'
               ,'MASCULINO','Casado(a) Sociedad Conyugal','Divorciado(a)','Soltero(a)',
                    'Unión Libre','Viudo(a)']]
bmi_y_test = datar[['MALO']]

regr = linear_model.LinearRegression()

# 3.-FIT MODELO
regr.fit(bmi_X_train, bmi_y_test)

# 4.-PREDICCION

bmi_y_pred = regr.predict(bmi_X_train)

plt.scatter(bmi_X_train['ANT_DOM_MESES'], bmi_y_pred,  color='black')
print(bmi_y_pred)
plt.show()

# 5.- matriz de confusion



print('finsish!!')


































