from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conn.close()
    return render_template('index.html', alunos=alunos)

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    idade = request.form['idade']
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", (nome, idade))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete<int:aluno_id>', methods=['POST'])
def deletar(aluno_id):
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM alunos WHERE = id ?', (aluno_id))
    
    conn.commit()
    conn.close()
    return redirect(url_for('index.html'))



app.run(debug=True)