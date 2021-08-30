import os
from datetime import datetime

from pytz import timezone
from flask import Flask, render_template

app = Flask(__name__)

time_format = os.environ.get('TIME_FORMAT', '%H:%M:%S')

def get_msc_time():
    time = datetime.now(timezone('Europe/Moscow')).strftime(time_format)
    return time


@app.route("/")
def index():
    time = datetime.now(timezone('Europe/Moscow')).strftime(time_format)
    return render_template('index.html', time=time)