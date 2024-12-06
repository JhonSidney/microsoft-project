from flask import Blueprint

# Cria o blueprint 'alunos' e especifica a pasta de templates
alunos = Blueprint('alunos', __name__, template_folder='templates')

# Importa as rotas do arquivo routes.py
from . import routes