from flask import render_template, session, redirect, url_for, flash, request
from . import db
from .models import db, Curso, Ocorrencia  # Importando o modelo Ocorrencia
from flask import Blueprint
from datetime import datetime, timedelta, timezone

main = Blueprint('main', __name__)

# Página principal
@main.route('/', methods=['GET', 'POST'])
def index():
    brasilia_offset = timezone(timedelta(hours=-3))
    current_time = datetime.now(brasilia_offset)
    formatted_time = current_time.strftime('%B %d, %Y')
    return render_template('index.html', current_time=formatted_time)

# Página de cursos
@main.route('/cursos', methods=['GET', 'POST'])
def cursos():
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')

        novo_curso = Curso(nome=nome, descricao=descricao)
        db.session.add(novo_curso)
        db.session.commit()

        return redirect(url_for('main.cursos'))

    cursos = Curso.query.all()
    return render_template('cursos.html', cursos=cursos)

# Página de cadastro e exibição de ocorrências
@main.route('/ocorrencias', methods=['GET', 'POST'])
def ocorrencias():
    if request.method == 'POST':
        disciplina = request.form.get('disciplina')
        descricao = request.form.get('descricao')
        data = request.form.get('data')

        # Convertendo data do formulário para datetime
        if data:
            data_ocorrencia = datetime.strptime(data, '%d/%m/%Y' )

        nova_ocorrencia = Ocorrencia(disciplina=disciplina, data=data_ocorrencia, descricao=descricao)
        db.session.add(nova_ocorrencia)
        db.session.commit()

        flash('Ocorrência cadastrada com sucesso!')
        return redirect(url_for('main.ocorrencias'))

    ocorrencias = Ocorrencia.query.order_by(Ocorrencia.data.desc()).all()
    return render_template('ocorrencias.html', ocorrencias=ocorrencias)

# Tratamento de erros
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
