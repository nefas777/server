CONFIG = { 
  'mode': 'wsgi',
  'working_dir': '/home/box/web/hello.py',
  'args': (
      '--bind=0.0.0.0:8080',
      'hello.app'
  )
}
