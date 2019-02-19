release: python django-server/fras/manage.py migrate && python django-server/fras/manage.py createcachetable
web: gunicorn --chdir django-server/fras fras.wsgi
