from functools import wraps
from sqlalchemy.orm import Session
from typing import Callable, Any
from src.shared import database_connection

def with_read_session(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        session: Session = database_connection.get_session()
        try:
            return func(session=session, *args, **kwargs)
        finally:
            session.close()
    return wrapper

def with_write_session(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        session: Session = database_connection.get_session()
        try:
            return func(session=session, *args, **kwargs)
        finally:
            session.close()
    return wrapper

