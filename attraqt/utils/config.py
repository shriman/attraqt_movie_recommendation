# -*- coding: utf-8 -*-
"""
Config manager
"""
import os
import yaml
import logging
from box import Box
from pydantic import BaseSettings, BaseModel

logger = logging.getLogger(__name__)


class DataSources(BaseModel):
    movies_metadata: str
    ratings: str
    evaluation_ratings: str
    true_ratings: str


class OutputSources(BaseModel):
    submission: str
    bonus_submission: str


class TrainedModel(BaseModel):
    trained_model_path: str


class Config(BaseSettings):
    data: DataSources
    output: OutputSources
    model: TrainedModel


def load_config_file(yaml_file: str):
    """Parses a list of configuration files.

    Args:
        yaml_file: YAML file to parse.

    Returns:
        A Pydantic object containing the parsed configuration.
    """
    logger.info("Setting configuration files handler")
    logger.info("Loading YAML files: %s", yaml_file)
    config = Box()
    for config_file in yaml_file:
        if os.path.isfile(config_file) and os.access(config_file, os.R_OK):
            with open(config_file, "r") as stream:
                config_dict = yaml.load(stream, Loader=yaml.FullLoader)
                config.update(Box(config_dict))
        else:
            raise FileNotFoundError(config_file)

    config_obj = Config(**config.to_dict())
    return config_obj
