from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

alunos = []




@app.route('/')
def index():
    return render_template('index.html', alunos=alunos)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    idade = request.form['idade']
    email = request.form['email']

    alunos.append({'nome':nome, 'idade':idade, 'email':email})

    return redirect(url_for('index'))
app.run(debug=True)