from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Inicializa o objeto db
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Carrega a configuração do arquivo config.py

    # Inicializa o db com o app
    db.init_app(app)
    migrate.init_app(app, db)

    # Importa e registra o blueprint dos CRUDs depois que o app é criado
    from .alunos import alunos as alunos_blueprint
    app.register_blueprint(alunos_blueprint, url_prefix='/alunos')

    # Importa e registra as rotas principais do app
    from . import routes
    routes.init_app(app)

    return app
