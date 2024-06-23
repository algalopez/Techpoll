import logging

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.shared import registry, configuration

REGISTRY_NAME = 'database_engine'
BASE_NAME = "database_base"
BASE = declarative_base()


def load():
    logging.info(f"Loading database engine")

    database_config = registry.get(configuration.REGISTRY_NAME).get('database')

    user = database_config.get('user')
    password = database_config.get('password')
    host = database_config.get('host')
    port = database_config.get('port')
    database = database_config.get('database')
    engine = sqlalchemy.create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
    BASE.metadata.bind = engine
    registry.register(REGISTRY_NAME, engine)
    return engine


def get_session():
    engine = registry.get(REGISTRY_NAME)
    factory = sessionmaker(bind=engine)
    return factory()


def close_session(session):
    session.close()


def query_session(func):
    def wrapper(*args, **kwargs):
        session = get_session()
        try:
            func(*args, **kwargs)
        finally:
            session.close()

    return wrapper


def command_session(func):
    def wrapper(*args, **kwargs):
        session = get_session()
        try:
            func(*args, **kwargs)
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    return wrapper