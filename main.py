import pandas as pd
import numpy as np
import streamlit as st
from sklearn import linear_model

with open('path.txt', 'r') as f:
  path = f.read()

df = pd.read_csv(path)
model = linear_model.LinearRegression()

# Global GDP ------
columns = df.columns.values[1:]
x = np.array([int(column) for column in columns]).reshape(-1, 1)
y = np.array([df[column].mean() for column in columns])

countries_list = df['Country'].values

model.fit(x, y)
available_years = list(range(2015, 2031))

def predict_country_gpd(country: str) -> pd.DataFrame:
  country_model = linear_model.LinearRegression()
  known_values = np.array(df.loc[df['Country'] == country, columns].values.flatten())
  country_model.fit(x, known_values)
  country_prediction_before = country_model.predict(np.array(available_years[:5]).reshape(-1, 1))
  country_predictions_after = country_model.predict(np.array(available_years[11:]).reshape(-1, 1))
  country_prediction= np.concatenate((country_prediction_before, known_values, country_predictions_after), axis=0)
  return country_prediction


predictions_before = model.predict(np.array(available_years[:5]).reshape(-1, 1))
predictions_after = model.predict(np.array(available_years[11:]).reshape(-1, 1))
global_predictions = np.concatenate((predictions_before, y, predictions_after), axis=0)
predictions = pd.DataFrame({'Year': available_years, 'Prediction': global_predictions}).set_index('Year')

# Countries GDP
countries = ['Brazil', 'United States', 'Russia', 'China', 'Germany', 'Japan', 'United Kingdom', 'Italy', 'France', 'India', 'Canada']
countries_predictions = {}

for country in countries:
  countries_predictions[country] = predict_country_gpd(country)

countries.append('Global')
countries_predictions['Global'] = global_predictions

predictions = pd.DataFrame(data=countries_predictions, index=available_years, columns=countries)

# Streamlit -----

st.title("Predicting GDP through Linear Regression")
st.divider()

st.write("""Predicted GDP of certain countries and the Global mean. The values between [2020, 2025] are actually the real
         values used for training the model.""")
st.line_chart(predictions)
st.divider()

st.write('Visualize the GDP of a specific country:')
country = st.selectbox('Select a country', countries_list, index=10)
if country:
  country_prediction = predict_country_gpd(country)
  st.line_chart(pd.DataFrame({'GDP': country_prediction, 'Year': available_years}).set_index('Year'))
