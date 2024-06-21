from src.hello import hello


def run(request):
    return hello.Hello(name=request)
