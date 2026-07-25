# mobile_price_predictor
# 📱 Mobile Price Range Predictor

Predicts a mobile phone's price category (Low / Medium / High / Very High) based on its specifications, using a machine learning model trained on 2000 devices.

## Model Details
- **Algorithms compared:** Logistic Regression, Random Forest, XGBoost
- **Best model:** Logistic Regression
- **Tuning:** Multiple models compared using Accuracy, Precision, Recall, F1 (weighted)
- **Dataset:** Mobile Price Classification (Kaggle), 2000 records, 20 features

## Live App
[Yahan apna streamlit link aayega deploy hone ke baad]

## Tech Stack
Python, scikit-learn, XGBoost, Streamlit

## How to Run Locally
```
pip install -r requirements.txt
streamlit run app.py
```
