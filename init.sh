sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn_django.conf.py   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
sudo gunicorn --bind 0.0.0.0:8000 --access-logfile acc.log --error-logfile err.log ask.wsgi:application
