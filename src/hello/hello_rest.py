from flask import Blueprint
from src.hello import get_hello
import jsonpickle

hello_resource = Blueprint('hello_resource', __name__)


@hello_resource.route('/rest/hello/', defaults={'name': 'world'})
@hello_resource.route('/rest/hello/<name>')
def get(name):
    return jsonpickle.encode(get_hello.run(name), unpicklable=False)
