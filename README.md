# PROJETO SESI 
## PACOTES INTALADOS 
- pip install flask Flask-SQLAlchemy Flask-Migrate flask-login werkzeug

### Configuração inicial

### Certifique-se de configurar o arquivo .env (se necessário) com as informações sensíveis no caso estao em .config, para banco de dados.
### Execute as migrações do banco de dados antes de executar o python3 run.py:

- flask db init
- flask db migrate -m "Initial migration"
- flask db upgrade
