print('In Gunicorn config')
CONFIG = { 
  'mode': 'wsgi',
  'working_dir': '/home/box/web',
  'pythonpath' : '/home/box/web/ask',
  'args': (
      '--bind=0.0.0.0:8000',
      'wsgi:application'
  )
}
