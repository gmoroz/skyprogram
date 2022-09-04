from project.main.views import main_blueprint
from flask import Flask, send_from_directory

app = Flask(__name__)

app.register_blueprint(main_blueprint)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("project/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)
