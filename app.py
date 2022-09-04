import logging
from project.main.views import main_blueprint
from project.api.views import api_blueprint
from project.bookmarks.views import bookmarks_blueprint
from flask import Flask

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.static_folder = app.root_path + "/project/static/"

logging.basicConfig(filename="api.log", level=logging.INFO, encoding="utf-8")
logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")

if __name__ == "__main__":
    app.run(debug=True)
