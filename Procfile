release: python code/django-server/fras/manage.py migrate && python code/django-server/fras/manage.py createcachetable
web: gunicorn code.django-server.fras.fras.wsgi
