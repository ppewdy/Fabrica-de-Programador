from flask import Flask, render_template, request, redirect, url_for #importa o Flask, render_template, request, redirect, url_for
import sqlite3 #importa o bd

app = Flask(__name__)

def init_db():#define uma função
    conn = sqlite3.connect("alunos.db")#conecta com o alunos.db, se não tiver o bd criado ele cria
    cursor = conn.cursor()#pega as funções execute
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    ''')#cria uma tabela com id sendo um inteiro e uma pk, nome como texto obrigatório, idade um inteiro obrigatório
    conn.commit()#salva os comandos
    conn.close()#fecha o bd

init_db()#inicia a função



@app.route('/')#cria uma rota
def index():
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")#seleciona todos os itens da tabela alunos
    alunos = cursor.fetchall()#pega todos os itens e transforma em json
    conn.close()#fecha o bd
    return render_template('index.html', alunos=alunos)#retorna para o index

@app.route('/cadastro', methods=['POST'])#cria uma rota que vai usar o POST
def cadastro():
    nome = request.form['nome']#pega o nome do html e atribui a uma variavel
    idade = request.form['idade']#pega a idade do html e atribui a uma variavel
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", (nome, idade))#insere esses valores na tabela
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/deletar/<int:aluno_id>', methods=['POST'])
def deletar(aluno_id):
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))#deleta uma linha aonde tem o id especificado
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/editar/<int:aluno_id>')
def editar(aluno_id):
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,))
    aluno = cursor.fetchone()#traz uma informação para um o formato json
    conn.close()

    return render_template("editar.html", aluno=aluno)


@app.route('/editar/<int:aluno_id>', methods=['POST'])
def salvar_edicao(aluno_id):
    nome = request.form['nome']
    idade = request.form['idade']

    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE alunos SET nome = ?, idade = ? WHERE id = ?
    """, (nome, idade, aluno_id))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

app.run(debug=True)
