def app(environ, start_response):
  status = '200 OK'
  headers = [("Content-Type", "text/plain")]
  d = '\n'.join(environ['QUERY_STRING'].split('&'))
  print(d)
  start_response(status, headers)
  return [d]
