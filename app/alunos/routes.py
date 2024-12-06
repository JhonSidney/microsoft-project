from flask import render_template
from flask_login import login_required, current_user
from . import alunos  # Importa o blueprint existente

@alunos.route('/')
@login_required  # Protege a rota, exigindo que o usuário esteja autenticado
def index():
    print(f'Usuário atual: {current_user}') 
    return render_template('alunos/index.html')

# from flask import Blueprint, render_template
# from ..models import Aluno
# from . import alunos
# from flask_login import login_required

# alunos = Blueprint('alunos', __name__)

# @alunos.route('/')
# def index():
#     return render_template('alunos/index.html')




# @alunos.route('/create', methods=['GET', 'POST'])
# def create():
#     if request.method == 'POST':
#         nome = request.form['nome']
#         matricula = request.form['matricula']
        
#         novo_aluno = Aluno(nome=nome, matricula=matricula)
#         db.session.add(novo_aluno)
#         db.session.commit()
        
#         return redirect(url_for('alunos.index'))
#     return render_template('alunos/create.html')

# @alunos.route('/edit/<int:id>', methods=['GET', 'POST'])
# def edit(id):
#     aluno = Aluno.query.get(id)
#     if request.method == 'POST':
#         aluno.nome = request.form['nome']
#         aluno.matricula = request.form['matricula']
#         db.session.commit()
#         return redirect(url_for('alunos.index'))
#     return render_template('alunos/edit.html', aluno=aluno)

# @alunos.route('/delete/<int:id>')
# def delete(id):
#     aluno = Aluno.query.get(id)
#     db.session.delete(aluno)
#     db.session.commit()
#     return redirect(url_for('alunos.index'))
