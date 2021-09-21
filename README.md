# Descrição

Rest API com Python, Flask, com banco de dados SQLAlchemy e JWT que disponibiliza um token de acesso. Possui os métodos GET (listar todas contas), DELETE (deletar uma conta), POST (cadastro de uma conta), POST (login da conta - libera o token), POST (loggout da conta - requer o token), GET (listar todos os usuários e listar usuários por id), POST (cadastrar usuario inserindo os dados: usuario_id, nome, idade, cidade e rede_id - requer o token), PUT (atualizar usuários por id - requer o token), DELETE (deletar usuários por id - requer o token), GET (listar redes e listar redes por id), POST (criar redes inserindo a URL - requer o token) e DELETE (deletar a rede pela URL - requer o token).

OBs: É possível criar contas através do cadastro, dentro de uma conta é possível criar várias redes e dentro de uma rede é possível criar vários usuarios.

# Comandos no terminal para configuração

```bash
python setup.py develop
```

# Rodando a aplicação

```bash
python principal.py
```

# Teste no Postman

<span align="center">
    <img src="https://user-images.githubusercontent.com/85804895/134187850-078d4e91-50f1-42a8-9a6a-9e13075e9835.png", width=900>
</span>

<span align="center">
    <img src="https://user-images.githubusercontent.com/85804895/134187933-1eb81bdf-b007-447a-8eb2-a13c0539cad8.png", width=900>
</span>

<span align="center">
    <img src="https://user-images.githubusercontent.com/85804895/134188018-3b06c0a0-4a53-4181-97ee-121ffe2ed9d5.png", width=900>
</span>

