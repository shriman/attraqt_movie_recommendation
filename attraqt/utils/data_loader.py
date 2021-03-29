# -*- coding: utf-8 -*-
from cached_property import cached_property
import pandas as pd
import logging

from attraqt.utils.config import Config

logger = logging.getLogger(__name__)


def read_csv_file(file_path):
    return pd.read_csv(file_path)


def write_csv_file(data, file_path, sep=","):
    data.to_csv(file_path, sep, index=False)


class DataManager:
    """
    Class to load all data files
    """

    def __init__(self, config: Config):
        self.config = config
        self._load()

    def _load(
        self,
    ):
        logger.info("loading datasets")
        self._movies_metadata = read_csv_file(self.config.data.movies_metadata)
        self._ratings = read_csv_file(self.config.data.ratings)
        self._evaluation_ratings = read_csv_file(self.config.data.evaluation_ratings)
        self._true_ratings = read_csv_file(self.config.data.true_ratings)
        self._submission = read_csv_file(self.config.data.submission)

    @cached_property
    def movies_metadata(self):
        # clean the ids in the movies meta data, as some of the ids are in date format
        movies_metadata_df = self._movies_metadata
        movies_metadata_df["id"] = movies_metadata_df["id"].str.replace("-", "")
        movies_metadata_df["id"] = movies_metadata_df["id"].astype(int)
        return movies_metadata_df

    @cached_property
    def ratings(self):
        return self._ratings

    @cached_property
    def evaluation_ratings(self):
        return self._evaluation_ratings

    @cached_property
    def true_ratings(self):
        return self._true_ratings

    @cached_property
    def submission(self):
        return self._submission
