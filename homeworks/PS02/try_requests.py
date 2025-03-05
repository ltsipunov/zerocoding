import requests,pprint

def do_request(params):
    function = [requests.get,requests.post][params.pop('type','get')=='post']
    url = params.pop('url')
    response = function(url,params )
    pprint.pprint(response.json())

placeholder = 'https://jsonplaceholder.typicode.com/posts'
for p in [
    {'url': 'https://api.github.com'},
    { 'userId': '1', 'url':placeholder},
    {'title': 'foo', 'body': 'bar', 'userId': 1,'type':'post','url':placeholder}
]:
    do_request(p)
