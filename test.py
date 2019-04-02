import pandas as pd
import io
import requests
url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))
print('finish')

demograficos=pd.read_csv('C:/Users/BRM00000/Desktop/LGG_MRP_DEMOGRAFICAS_BADRATE_2.csv',encoding='cp1252')
print(demograficos)

enc  =  OneHotEncoder ( handle_unknown = 'ignore' )
X  =  [[ 'casado(a)Separación de Bienes' ,  1 ],  [ 'Divorciado' ,  2 ],  [ 'Soltero' ,  3 ]]
enc . ajuste ( X )
data[GENERO["masculino","FEMENINO"]]