from flask import Blueprint
from src.hello import get_hello_actor
import jsonpickle

get_hello_resource = Blueprint('get_hello_resource', __name__)


@get_hello_resource.route('/rest/hello/', defaults={'name': 'world'})
@get_hello_resource.route('/rest/hello/<name>')
def get(name):
    return jsonpickle.encode(get_hello_actor.run(name), unpicklable=False)
