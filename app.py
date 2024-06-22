from flask import Flask
from src.hello import get_hello_rest
from src.poll import post_results_rest
from src.config import configuration


import logging


def add_resources_endpoints(flask_app):
    flask_app.register_blueprint(get_hello_rest.get_hello_resource)
    flask_app.register_blueprint(post_results_rest.post_results_resource)

def set_logger_format():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(levelname)-8s > %(message)s", datefmt="%I:%M:%S")

def start():
    set_logger_format()
    app_config = configuration.load(configuration.APP_CONFIG)
    flask_app = Flask(__name__)
    flask_app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    add_resources_endpoints(flask_app)
    flask_app.run(host='0.0.0.0', port=app_config.get('port'), debug=True)


if __name__ == '__main__':
    start()