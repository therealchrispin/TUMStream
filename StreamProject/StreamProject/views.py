from pyramid.view import view_config, view_defaults
from StreamProject.ItemCreator.ItemCreatorService import *


@view_defaults(renderer="")
class ItemServices:
    def __init__(self, request):
        self.request = request

    @view_config(route_name="itemservice.json", renderer="json", request_method="POST")
    def createItemFromJson(self):
        data = self.request.POST
        ItemCreatorService.create_item_from_json(data)

        return {'data': data}
