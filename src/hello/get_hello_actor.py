from src.hello import hello


def run(request):
    """
    Get a list

    :param request: A list id
    :return: The list
    """
    return hello.Hello(name=request)
