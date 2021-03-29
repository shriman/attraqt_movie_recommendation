# -*- coding: utf-8 -*-
import logging
from sklearn.metrics import mean_squared_error

logger = logging.getLogger(__name__)


def get_rmse(y_test, y_pred):
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    logger.info("The root mean squared error (RMSE) on test set: {:.6f}".format(rmse))
    return rmse
