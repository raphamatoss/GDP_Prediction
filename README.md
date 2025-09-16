# 🌍 Global & Country GDP Prediction Dashboard
![gdp](https://github.com/user-attachments/assets/df3f47c4-e671-41d1-a67f-fad8831402c7)

An interactive **Streamlit web app** that predicts **Global and Country GDP** trends using **Linear Regression (scikit-learn)**. The project demonstrates how machine learning can be applied to economic data visualization and forecasting.
[View the dataset used on Kaggle](https://www.kaggle.com/datasets/codebynadiia/gdp-per-country-20202025)

---

## 🚀 Features
- 📈 **Global GDP Forecasts** – aggregate world GDP trends with future projections up to 2030
- 🏳️ **Country-Level Predictions** – trained models for top 10 global economies
- 🔍 **Historical vs Predicted Data** – compare actual GDP values with regression-based forecasts
- 📊 **Interactive Dashboards** – built with Streamlit for easy exploration
- ⚡ **Lightweight ML** – linear regression models trained with `scikit-learn`

---

## 🛠️ Tech Stack
- **Python 3**  
- **Pandas** – data processing  
- **NumPy** – numerical computations  
- **scikit-learn** – linear regression modeling  
- **Streamlit** – interactive dashboards and visualization  

---

## 📂 Project Structure
├── main.py # Streamlit app entry point

├── gdp_dataset.csv # Dataset used for training 

├── requirements.txt # Python dependencies

└── README.md # Project documentation

---

## ▶️ Running the App
You can run the app locally or open it in the [web](https://gdp-prediction.streamlit.app/).

```bash
# Clone the repository
git clone https://github.com/raphamatoss/GDP_Prediction.git
cd GDP_Prediction

# Install dependencies
pip install -r requirements.txt

# Run Streamlit
streamlit run main.py
