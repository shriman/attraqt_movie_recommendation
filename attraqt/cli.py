import logging
import click

from attraqt.model import train, predict_ratings, evaluate_submission
from attraqt.utils.config import load_config_file

logger = logging.getLogger(__name__)


class ConfigReader:
    def __init__(self, configuration_files: [str]):
        self._configuration_files = configuration_files

    def get_config_file(self, **kwargs) -> [str]:
        """Get the configuration files, expanded using `str.format`.

        This allows to have configuration file paths with dynamic fields, such as {filenames}.

        >>> cfg = ConfigReader(["configs/config.yml"])
        >>> cfg.get_config_file()
        ["configs/config.yml"]
        """
        return [value.format(**kwargs) for value in self._configuration_files]


@click.group()
@click.option(
    "--config-file",
    default=["configs/config.yml"],
)
@click.pass_context
def cli(context, config_file: [str]):
    context.ensure_object(dict)
    context.obj["config_file"] = ConfigReader(config_file)


@cli.command()
@click.pass_context
def train(context):
    config_file = context.obj["config_file"].get_config_file()
    config = load_config_file(config_file)
    logger.info("config file: ", config_file)
    logger.info("config", config)
    train(config)


@cli.command()
@click.pass_context
def predict(context):
    config_file = context.obj["config_file"].get_config_file()
    config = load_config_file(config_file)
    logger.info("config file: ", config_file)
    logger.info("config", config)
    print("random")
    logger.info("Running the test program")
    predict_ratings(config)


@cli.command()
@click.pass_context
def evaluate(context):
    config_file = context.obj["config_file"].get_config_file()
    config = load_config_file(config_file)
    logger.info("config file: ", config_file)
    logger.info("config", config)
    print("random")
    logger.info("Running the evaluation")
    evaluate_submission(config)
