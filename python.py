from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


clientes = []
produtos = []


@app.route('/')
def index():
    return render_template('index.html', clientes=clientes, produtos=produtos)

# Rota para cadastrar um novo cliente
@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    nome = request.form['nome']
    email = request.form['email']
    clientes.append({'nome': nome, 'email': email})
    return redirect(url_for('index'))

# Rota para cadastrar um novo produto
@app.route('/cadastrar_produto', methods=['POST'])
def cadastrar_produto():
    nome_produto = request.form['nome_produto']
    preco_produto = request.form['preco_produto']
    produtos.append({'nome_produto': nome_produto, 'preco_produto': preco_produto})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)