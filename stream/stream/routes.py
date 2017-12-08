def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('itemcreator-json', 'itemcreator.json')
    config.add_route('json-stream', 'stream.json')
