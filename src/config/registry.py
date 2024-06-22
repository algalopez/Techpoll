registry = dict()


def register(name, element):
    registry[name] = element

def un_register(name):
    registry.pop(name)

def get(name):
    return registry.get(name)
