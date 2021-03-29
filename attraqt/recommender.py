# -*- coding: utf-8 -*-
import pandas as pd
import logging

from surprise import Dataset, SVD, Reader, dump
from surprise.model_selection import GridSearchCV

logger = logging.getLogger(__name__)


def main(ratings_df: pd.DataFrame):

    logger.info(
        "Running grid search to find the optimal hyper parameters for the recommender"
    )
    reader = Reader()
    data = Dataset.load_from_df(ratings_df[["userId", "movieId", "rating"]], reader)

    param_grid = {"n_epochs": [5, 10], "lr_all": [0.002, 0.005], "reg_all": [0.4, 0.6]}
    grid_search = GridSearchCV(SVD, param_grid, measures=["rmse", "mae"], cv=5)

    # This takes 3 hours on my local machine, need to find a way to optimize it
    logger.info("This might take some time! (depending on the size of the machine)")
    grid_search.fit(data)

    # best RMSE score
    logger.info(grid_search.best_score["rmse"])

    # combination of parameters that gave the best RMSE score
    logger.info(grid_search.best_params["rmse"])

    recommender = grid_search.best_estimator["rmse"]
    recommender.fit(data.build_full_trainset())

    logger.info(
        "Finished running the grid search and found the optimal hyper paramters"
    )

    return recommender


def save_model(trained_model_path, trained_model):
    dump.dump(trained_model_path, trained_model)


def load_model(trained_model_path):
    _, recommender = dump.load(trained_model_path)
    return recommender
