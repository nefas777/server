from cgi 
def app(environ, start_response):
  status = '200 OK'
  headers = [("Content-Type", "text/plain")]
  d = parse_qs(environ['QUERY_STRING'])
  string = ''
  for k in d:
    string += k+'='+str(d[k])
  start_response(status, headers)
  return [string]
