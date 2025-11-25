from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

alunos=[ {'nome':'Gabriel',
        'idade':16
 },
 {'nome':'murilo',
        'idade':16,
    'id':11    

 }  ]
@app.route('/')
def index():

    return render_template('index.html', resultado =alunos)

@app.route("/Adicionar", methods=['POST'])
def Adicionar():
    # o codigo abaixo captura os valores do input usando request 
    nome = request.form[nome]
    idade = request.form[idade]
    telefone = request.form[telefone]

    alunos.append(
        {'nome':nome,
          'idade':idade,
            'telefone':telefone}
        
        )
    return redirect(url_for('index'))
    


app.run(debug=True)