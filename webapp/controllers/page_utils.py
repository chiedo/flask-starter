def global_tasks(request):
    """Performs all the tasks that should happen on every page"""
    return 'stub'


def global_args(request):
    """Arguments that should be passed to all pages"""
    kwargs = {'bar': 'foo', 'foo': 'bar'}
    return kwargs
