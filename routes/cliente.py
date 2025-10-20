from flask import Blueprint, render_template, request
from database.models.cliente import Cliente 

cliente_route = Blueprint('cliente', __name__)

"""
Rotas para gerenciamento de clientes:
    /clientes/ (GET) - Listar os clientes
    /clientes/ (POST) - inserir o cliente no servidor
    /clientes/new (GET) - renderizar o formulário para criar um cliente
    /clientes/:id (GET) - obter os dados de um cliente
    /clientes/:id/edit (GET) - renderizar um formulário para editar um cliente
    /clientes/:id/update (PUT) - atualizar os dados do cliente
    /clientes/:id/delete (DELETE) - deleta o registro do usuario
"""

@cliente_route.route('/')
def lista_clientes():
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    data = request.json

    novo_usuario = Cliente.create(
        nome=data.get("nome"),
        email=data.get("email")
    )

    return render_template('item_client.html', cliente=novo_usuario), 201
    

@cliente_route.route('/new')
def form_cliente():
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):

    cliente=Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):

    cliente=Cliente.get_by_id(cliente_id)
    return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    data = request.json

    cliente_editado=Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data.get("nome")
    cliente_editado.email = data.get("email")
    cliente_editado.save()

    return render_template('item_client.html', cliente=cliente_editado), 200

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    cliente=Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return 'Deleted client', 204