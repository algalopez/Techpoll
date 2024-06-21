import yaml
import os
import logging
from src import registry


REGISTRY_NAME = 'app_config'
APP_CONFIG = 'app.yaml'
TEST_CONFIG = 'app-test.yaml'


def load(filename):
    logging.info(f"Loading {filename} configuration file")
    app_config = __read_file(filename)
    registry.register(REGISTRY_NAME, app_config)
    return app_config


def __read_file(filename):
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, '../configuration', filename)
    with open(path) as file:
        return yaml.load(file, Loader=yaml.FullLoader)
