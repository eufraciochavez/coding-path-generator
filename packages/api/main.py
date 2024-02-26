import os

from fastapi import FastAPI
from importlib.util import find_spec

from core.wsgi import application as django_app
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


app = FastAPI()


app.mount(
        '/django/static',
        StaticFiles(
            directory=os.path.normpath(
                os.path.join(find_spec('django.contrib.admin').origin, '..', 'static')
            )
        ),
        name='static',
    )

app.mount("/django", WSGIMiddleware(django_app))


@app.get("/")
def read_root():
    return {"Hello": "World"}