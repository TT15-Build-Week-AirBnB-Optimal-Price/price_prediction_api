"""
Price functions
  predict_price()
"""
import random
import logging
from app.schemas.listing import Listing
from joblib import load

log = logging.getLogger(__name__)
pipeline = load("app/ml_models/working_model.sav")


def predict_price(listing: Listing):
    """
    Function to predict price, based on a provided Listing
    """
    X_new = listing.to_df()
    log.info(X_new)
    y_pred = pipeline.predict(X_new)
    return {
        'prediction': y_pred[0]
    }
