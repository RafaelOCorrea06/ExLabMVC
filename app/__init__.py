from pathlib import Path
from flask import Flask


def create_app():
    base_dir = Path(__file__).resolve().parent

    app = Flask(
        __name__,
        template_folder=str(base_dir / "views"),
        static_folder=str(base_dir / "static"),
    )

    from app.controllers.livro_controller import livro_bp
    app.register_blueprint(livro_bp)

    return app