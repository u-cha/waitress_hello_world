from waitress import serve


def wsgi_app(environ, start_fn):
    status = '200 OK'
    headers_list = [('Content-Type', 'text/plain')]
    start_fn(status, headers_list)
    response_text = "Hello, Kotofey!\nHello, Kotofeyushka"
    response_body = bytes(response_text, encoding='utf-8')
    return [response_body]


serve(wsgi_app, host='localhost', port=8080)

