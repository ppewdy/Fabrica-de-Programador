from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)

def conect():
    
    #cria ou abre um banco de dados
    conn=sqlite3.connect('alunos.db')
    #permite usar uns comando ai, execute e tals
    comandoSql = conn.cursor()
    #deixa vc coisar o sql ó
    comandoSql.execute('''CREATE TABLE agendamento (nome TEXT ,idade INTEGER , peso REAL , horario DATE)''')
    #manda as coisas pro bd
    conn.commit()
    #fecha
    conn.close()
conect()

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/agendar', methods=['POST'])
def agendar():
    nome = request.form['nome']
    idade = request.form['idade']
    peso = request.form['peso']
    horario = request.form['horario']
    
    
    conn=sqlite3.connect('alunos.db')
    cursor = conn.cursor()

    #tem que colocar ?
    cursor.execute('INSERT INTO agendamento (nome,idade,peso,horario)values(?,?,?,?)',(nome,idade,peso,horario))
    conn.commit()
    conn.close()
    return redirect(url_for('main'))

@app.route('/cadastro')
def cadastrar():
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()

    cursor.execute('SELECT FROM * alunos')
    alunos = cursor.fetchall()
    

    conn.commit()
    conn.close()











app.run(debug=True)