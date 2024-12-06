from flask import request, redirect, url_for, render_template, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Usuario, db
from flask_login import login_user, logout_user, login_required, current_user
import time


def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')  # Obtendo o email
            password = request.form.get('password')
            hashed_password = generate_password_hash(password)

            if email is None:
                flash('O email é obrigatório!', 'error')
                return redirect(url_for('register'))
            
            novo_usuario = Usuario(username=username, email=email, password=hashed_password)
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Usuário registrado com sucesso!')
            return redirect(url_for('login'))
        
        return render_template('register.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')  # Obtendo o email
            password = request.form.get('password')
            user = Usuario.query.filter_by(email=email).first()
            
            if user and check_password_hash(user.password, password):
                login_user(user)
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Usuário ou senha inválidos.', 'danger') 
        
        return render_template('login.html')
    
    @app.route('/dashboard')
    @login_required
    def dashboard():
        return render_template('dashboard.html')
    
    @app.route('/sobre')
    def sobre():
        return render_template('sobre.html')
    
    @app.route('/contato')
    def contato():
        return render_template('contato.html')
    
    @app.route('/contato')
    def unidades():
        return render_template('unidade.html')

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Logout realizado com sucesso!','success')
        return redirect(url_for('login'))
    


