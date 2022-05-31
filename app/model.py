import firebase_admin
from firebase_admin import credentials, firestore
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def model_builder() -> ExponentialSmoothing:
    """Helper function to asist in model building for forecasting.

    Returns:
        ExponentialSmoothing: A trained runnable model to be used for forecasting
    """
    df = pd.read_csv("data/nyc_crisis_may.csv")
    df.sort_values("date", inplace=True)

    return ExponentialSmoothing(
        df.crisis,
        seasonal_periods=7,
    ).fit()


forecaster = model_builder()

# init firestore connection
cred = credentials.Certificate("configs/app_creds.json")
firebase_admin.initialize_app(cred,
    {
        "databaseURL": "https://save-nyc-demo.firebaseio.com/"
    }
)

db = firestore.client()
