from flask import Flask, render_template, url_for

app = Flask(__name__)


# passo a passo para criar uma nova pagina
#route / funcao / html / barra


lista_usuarios = ['Diego', 'Douglas', 'Marcelle', 'Marie']

app.config['SECRET_KEY'] = 'exit65a7537d04071fe0650c19be550a2c90'


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/contato")
def contato():
    return render_template('contato.html')


@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route("/login-criar-conta")
def login_criar_conta():
    return render_template('login_criar_conta.html')




if __name__ == '__main__':
    app.run(debug=True)
