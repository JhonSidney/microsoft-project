# from flask import Blueprint, render_template
# from flask_login import login_required


# alunos = Blueprint('alunos', __name__, template_folder='templates')


# @alunos.route('/')
# @login_required  # Protege a rota, exigindo que o usuário esteja autenticado
# def index():
#     return render_template('alunos/index.html')

from flask import Blueprint

# Cria o blueprint 'alunos' e especifica a pasta de templates
alunos = Blueprint('alunos', __name__, template_folder='templates')

# Importa as rotas do arquivo routes.py
from . import routes