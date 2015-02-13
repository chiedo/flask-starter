def global_response_handler(request, response):
    """Can handle formatting of the page response"""
    return response


def global_args(request):
    """Arguments that can be passed to all pages"""
    kwargs = {'bar': 'foo', 'foo': 'bar'}
    return kwargs
