from pyramid.view import view_defaults, view_config
from stream.ItemCreator.ItemCreator import ItemCreator
from stream.ItemCreator.Parser import JSONParser


@view_defaults(renderer="../templates/main.jinja2")
class View:
    def __init__(self, request):
        self.request = request
        self.request.response.headers.update({
            'Access-Control-Allow-Origin': '*',
        })

    @view_config(route_name='home')
    def my_view(self):
        return {'project': 'Stream'}


class ItemBuilder(View):
    def __init__(self, request):
        View.__init__(self, request)
        self.item_creator = ItemCreator(self.request)


class JsonItem(ItemBuilder):
    def __init__(self, request):
        ItemBuilder.__init__(self, request)

    @view_config(route_name="itemcreator-json", renderer="json")
    def create_item_from_json(self):
        parser = JSONParser()
        self.item_creator.set_parser(parser)
        self.item_creator.set_data_object(self.request.POST['data'])
        try:
            self.item_creator.create_item()
        except ValueError:
            return {'message': "ValueError"}

        return {'message': 'Item Created'}

