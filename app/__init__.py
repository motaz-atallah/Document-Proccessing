from flask import Flask

from config import Config

def create_app():
    app = Flask(__name__)
    
    # Load configuration if needed
    app.config.from_object(Config)

    with app.app_context():
        from .routes import main  # Import and register routes
        app.register_blueprint(main)

    return app
