from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    os.system('seq 1 | xargs -P0 -n1 timeout 1 yes > /dev/null')
    now = datetime.now()
    now_strig = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    msg = "<p>Task completed: {}</p>".format(now_strig)
    return msg