contatos = {  'João': '123-456-7890',   'Maria': '987-654-3210',  'Jose': '999-999-999'}

nome_a_remover = 'Maria'


if nome_a_remover in contatos:
    del contatos[nome_a_remover]
    print(f'O contato {nome_a_remover} foi removido com sucesso.')
else:
    print(f'O contato {nome_a_remover} não foi encontrado.')


print(contatos)