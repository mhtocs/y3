from flask import Flask, jsonify
from dotenv import load_dotenv
from config import Config

import coloredlogs
from api import celery, init_celery


def submit_download_task(url):
    return "d18sa7h001"


def create_app():
    load_dotenv()
    app = Flask(__name__)
    coloredlogs.install(logger=app.logger)
    app.url_map.strict_slashes = True
    app.config.from_object(Config)
    init_celery(app, celery)

    @app.route("/")
    def index():
        return "Hello World!"

    @app.route("/download/<string:url>")
    def download(url):
        task_id = submit_download_task(url)

        return jsonify({
            "status": "success",
            "task_id": task_id,
            "message": f"Download started for {url}"
        })

    @app.route("/task/<string:task_id>")
    def task(task_id):
        return jsonify({
            "status": "done",
            "task_id": task_id,
            "link": "https://rr5---sn-cvh7knzl.googlevi"
        })

    return app
