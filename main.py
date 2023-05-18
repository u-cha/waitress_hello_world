from waitress import serve


def wsgi_app(environ, start_fn):
    status = '200 OK'
    headers_list = [('Content-Type', 'text/plain')]
    start_fn(status, headers_list)
    response_body = "Hello, Kotofey!\nHello, Kotofeyushka".encode('utf-8')
    return [response_body]


serve(wsgi_app, host='localhost', port=8080)

