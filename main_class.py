from waitress import serve

response = 'Hello Kotofey2'.encode()


class WSGIApp:

    def __init__(self, environ, start_fn):
        self.environ = environ
        self.start_fn = start_fn

    def __iter__(self):
        status = '200 OK'
        headers_list = [('Content-Type', 'text/plain')]
        self.start_fn(status, headers_list)
        yield response


serve(WSGIApp, host='127.0.0.2', port=3000)
