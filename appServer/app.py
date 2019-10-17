import datetime
def handler(environ, start_response):
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    headers = [('Content-Type', 'text/plain'),
        ('Content-Lenght', str(len(data)))]
    start_response('200 OK', headers)
    return [bytes(data, encoding='utf8')]
