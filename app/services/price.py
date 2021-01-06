"""
Price functions
  predict_price()
"""
import random
import logging
from app.schemas.listing import Listing
from joblib import load

log = logging.getLogger(__name__)
# pipeline = load("ml_models/pipeline.joblib")


def predict_price(listing: Listing):
    """
    Function to predict price, based on a provided Listing
    """
    X_new = listing.to_df()
    log.info(X_new)
    y_pred = random.uniform(30.0, 150.99)

    return {
        'prediction': y_pred
    }
