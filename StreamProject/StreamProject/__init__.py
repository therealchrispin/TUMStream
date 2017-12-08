from StreamProject.DbModel.models import DBSession, Base
from pyramid.config import Configurator
from sqlalchemy import engine_from_config


def main(global_config=None, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings, root_factory='StreamProject.ItemCreator.models.Root')
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('itemservice.json', '/createItem.json')
    config.scan()
    return config.make_wsgi_app()
