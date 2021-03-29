# -*- coding: utf-8 -*-
import pandas as pd
import logging

from attraqt.utils.config import Config
from attraqt.utils.data_loader import DataManager
import attraqt.recommender as recommender
from attraqt.metrics import get_rmse

logger = logging.getLogger(__name__)


def get_dataloader(config: Config):
    return DataManager(config=config)


def get_movie_ratings(config: Config):
    print(config)
    dataloader = get_dataloader(config)

    # Step 0. load the datasets
    movies_metadata = dataloader.movies_metadata
    ratings = dataloader.ratings
    evaluation_ratings = dataloader.evaluation_ratings

    # Step 1. Train the model
    optimized_recommender = recommender.main(ratings)

    # Step 2. Get the evaluation predictions
    evaluation_ratings["predictions"] = evaluation_ratings.apply(
        lambda x: optimized_recommender.predict(x.userId, x.movieId), axis=1
    )

    # Step 3. Process the output file
    evaluation_ratings["Rating"] = evaluation_ratings["predictions"].apply(
        lambda x: x.est
    )
    evaluation_ratings["was_impossible"] = evaluation_ratings["predictions"].apply(
        lambda x: x.details["was_impossible"]
    )

    # Step 4. Write the output to csv file
    submission = evaluation_ratings[["userId", "movieId", "Rating"]]
    submission.columns = ["UserId", "MovieId", "Rating"]
    submission.to_csv(config.data.submission)

    # Step 5. Evaluate the performance of the model with the true predictions
    true_ratings = dataloader.true_ratings

    metrics_data = pd.merge(
        submission,
        true_ratings,
        left_on=["UserId", "MovieId"],
        right_on=["UserId", "MovieId"],
        how="inner",
    )
    rmse = get_rmse(metrics_data[["Rating", "TrueRating"]])
    # TODO the name of the column shoudl be TrueRating
    logger.info("The root mean squared error (RMSE) on test set: {:.6f}".format(rmse))
