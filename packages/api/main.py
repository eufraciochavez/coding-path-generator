import os
from typing import Annotated
from fastapi import FastAPI
from importlib.util import find_spec
from django.apps import apps
from django.conf import settings

from core.wsgi import application as django_app
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.wsgi import WSGIMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
apps.populate(settings.INSTALLED_APPS)


app = FastAPI(debug=settings.DEBUG)


app.mount(
        '/django/static',
        StaticFiles(
            directory=os.path.normpath(
                os.path.join(find_spec('django.contrib.admin').origin, '..', 'static')
            )
        ),
        name='static',
    )

app.mount('/django', WSGIMiddleware(django_app))


@app.get('/')
def read_root():
    return {'Hello': 'World'}