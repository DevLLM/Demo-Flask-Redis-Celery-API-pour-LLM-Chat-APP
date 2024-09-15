from celery import Celery
from tasks import *

celery = Celery(
    'myapp',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)



