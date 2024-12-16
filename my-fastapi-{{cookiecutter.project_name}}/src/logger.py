# endregion-------------------------------------------------------------------------
# region LOGGING HANDLER
# ----------------------------------------------------------------------------------
import logging.config
import yaml  # type: ignore[import]
import sys
import os

from settings.config import Config
from pathlib import Path


def setup_logger(default_level=logging.INFO) -> None:
    config = Config()
    config_path = config.LOGGER_CONFIG_PATH

    if os.path.exists(config_path):
        with open(config_path, "rt") as f:
            config_logger = yaml.safe_load(f.read())

        logger_dir = Path("logs")
        logger_dir.mkdir(exist_ok=True)

        logging.config.dictConfig(config_logger)
    else:
        logging.basicConfig(
            level=default_level,
            stream=sys.stdout,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )


# endregion-------------------------------------------------------------------------
