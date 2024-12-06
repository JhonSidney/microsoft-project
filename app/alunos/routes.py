from flask import render_template
from . import alunos  # Importa o blueprint existente

@alunos.route('/')
def index():
    return render_template('alunos/index.html')