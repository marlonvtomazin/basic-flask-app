from flask import Flask, url_for, render_template

#inicializacao
app = Flask(__name__)

#rotas
@app.route('/')
def home():
    titulo = 'Gestão de usuários'
    usuarios = [
        {"nome": "Marlon", "membro_ativo": True},
        {"nome": "João", "membro_ativo": False},
        {"nome": "Gabriela", "membro_ativo": False},
    ]
    return render_template('index.html', titulo=titulo, usuarios=usuarios)

@app.route('/sobre')
def pagina_sobre():
    return """
        <h1>Sobre Mim</h1>
        <p>Meu nome é Marlon e esse é meu <a href="https://github.com/marlonvtomazin">Github</a>:  
    """


#exe
app.run(debug=True)

