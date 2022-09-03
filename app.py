from project.main.views import main_blueprint
from flask import Flask

app = Flask(__name__)

app.register_blueprint(main_blueprint)

if __name__ == "__main__":
    app.run(debug=True)