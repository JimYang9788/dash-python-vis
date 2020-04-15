from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__,
                instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():

        # Import main Blueprint
        from . import routes
        app.register_blueprint(routes.main_bp)

        # Import Dash application
        from .dash_application import dash_example
        app = dash_example.Add_Dash(app)

        return app

