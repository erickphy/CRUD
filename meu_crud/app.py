from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    vagas = db.Column(db.Integer, nullable=False)
    alunos = db.relationship('Aluno', backref='curso', lazy=True)

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)

@app.route('/cursos')
def listar_cursos():
    cursos = Curso.query.all()
    return render_template('cursos.html', cursos=cursos)

@app.route('/cursos/novo', methods=['GET', 'POST'])
def novo_curso():
    if request.method == 'POST':
        nome = request.form['nome']
        vagas = request.form['vagas']
        curso = Curso(nome=nome, vagas=int(vagas))
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('listar_cursos', acao='criar'))
    return render_template('novo_curso.html')

@app.route('/cursos/editar/<int:id>', methods=['GET', 'POST'])
def editar_curso(id):
    curso = Curso.query.get_or_404(id)
    if request.method == 'POST':
        curso.nome = request.form['nome']
        curso.vagas = int(request.form['vagas'])
        db.session.commit()
        return redirect(url_for('listar_cursos', acao='editar'))
    return render_template('editar_curso.html', curso=curso)

@app.route('/cursos/deletar/<int:id>')
def deletar_curso(id):
    curso = Curso.query.get_or_404(id)
    db.session.delete(curso)
    db.session.commit()
    return redirect(url_for('listar_cursos', acao='excluir'))

@app.route('/alunos')
def listar_alunos():
    alunos = Aluno.query.all()
    cursos = Curso.query.all()
    return render_template('alunos.html', alunos=alunos, cursos=cursos)

@app.route('/alunos/novo', methods=['GET', 'POST'])
def novo_aluno():
    cursos = Curso.query.all()
    if request.method == 'POST':
        nome = request.form['nome']
        matricula = request.form['matricula']
        curso_id = request.form['curso_id']
        aluno = Aluno(nome=nome, matricula=matricula, curso_id=int(curso_id))
        db.session.add(aluno)
        db.session.commit()
        return redirect(url_for('listar_alunos', acao='criar'))
    return render_template('novo_aluno.html', cursos=cursos)

@app.route('/alunos/editar/<int:id>', methods=['GET', 'POST'])
def editar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    cursos = Curso.query.all()
    if request.method == 'POST':
        aluno.nome = request.form['nome']
        aluno.matricula = request.form['matricula']
        aluno.curso_id = int(request.form['curso_id'])
        db.session.commit()
        return redirect(url_for('listar_alunos', acao='editar'))
    return render_template('editar_aluno.html', aluno=aluno, cursos=cursos)

@app.route('/alunos/deletar/<int:id>')
def deletar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('listar_alunos', acao='excluir'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)