from flask import Flask, redirect, url_for
from models.models import db
from auth.routes import auth_bp
from attendance.routes import attendance_bp
from config import Config
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(attendance_bp)

    # Root route - redirect to login
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    return app

# Run app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
