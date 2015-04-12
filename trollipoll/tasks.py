from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

@app.task
def poll_weather_website_api(site_url):
    return "ok"
