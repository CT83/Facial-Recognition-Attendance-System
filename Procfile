release: python code/django-server/fras/manage.py migrate && python code/django-server/fras/manage.py createcachetable
web: gunicorn --chdir code/django-server/fras fras.wsgi
