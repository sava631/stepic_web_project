sudo ln -s ~/web/etc/nginx.conf /etc/nginx/site-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s ~/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
