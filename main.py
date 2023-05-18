from waitress import serve


def wsgi_app(environ, start_fn):
    status = '200 OK'
    headers_list = [('Content-Type', 'text/plain')]
    start_fn(status, headers_list)
    return [b"Hello, Kotofey!\n", b"Hello, Kotofeyushka"]


serve(wsgi_app, host='localhost', port=8080)

