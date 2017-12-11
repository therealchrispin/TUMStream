from pyramid.view import view_config
from stream.StreamCreator.Stream import Stream
from stream.views.ItemBuilder import View


class BaseStreamCreator(View):
    def __init__(self, request):
        View.__init__(self, request)
        self.stream = Stream(request)


class JSONStreamCreator(BaseStreamCreator):
    def __init__(self, request):
        BaseStreamCreator.__init__(self, request)

    @view_config(route_name="json-stream", renderer='json')
    def get_stream(self):

        return {'itemList': self.stream.get_all()}
