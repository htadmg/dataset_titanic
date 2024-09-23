import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import accuracy_score
import joblib 

url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
dados = pd.read_csv(url)

print(dados.columns)

dados = dados.drop(columns=["Name"])

dados = dados.dropna(subset=["Age", "Fare"])

dados = pd.get_dummies(dados, columns=["Sex", "Pclass"], drop_first=True)

x = dados.drop(columns="Survived")

y = dados["Survived"]

x_train, x_teste, y_train, y_teste = train_test_split(x, y, test_size=0.2, random_state=432, stratify=y)

modelo = xgb.XGBClassifier(object="binary:logistic", eval_metric="logloss")
modelo.fit(x_train, y_train)

preds = modelo.predict(x_teste)

acuracia = accuracy_score(y_teste, preds)
print(f'A acurácia do modelo é: {acuracia:.2%}')

#salvando o modelo treinado 
joblib.dump(modelo, "modelo_titanic.pkl")
