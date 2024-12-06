from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager

# Inicializa o objeto db
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager() ##
login_manager.login_view = 'login' ##

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Carrega a configuração do arquivo config.py
    Bootstrap(app)

    # Inicializa o db com o app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)##

    @login_manager.user_loader
    def load_user(user_id):
        from .models import Usuario
        return Usuario.query.get(int(user_id))

    # Importa e registra o blueprint dos CRUDs depois que o app é criado
    from .alunos import alunos as alunos_blueprint
    app.register_blueprint(alunos_blueprint, url_prefix='/alunos')

    # Importa e registra as rotas principais do app
    from . import routes
    routes.init_app(app)

    return app