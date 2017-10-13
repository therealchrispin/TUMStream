import json
from StreamItem import StreamItem


item = StreamItem()

print(item.__dict__.keys())

test = '{"title":"test", "age":35}'

testo = json.loads(test)

print(type(testo['title']))
