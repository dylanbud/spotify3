from flask import Flask
def create_app():
    # initializes our app
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

        
    return app