def global_response_handler(request, response):
    """Handles Formatting of the response that should take place on all pages"""
    return response


def global_args(request):
    """Arguments that should be passed to all pages"""
    kwargs = {'bar': 'foo', 'foo': 'bar'}
    return kwargs
