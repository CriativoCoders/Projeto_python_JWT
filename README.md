# API de Usuários com Autenticação JWT

## Descrição

Esta é uma API RESTful para gerenciar usuários, permitindo operações de CRUD (Criar, Ler, Atualizar, Deletar) apenas para usuários autenticados. A autenticação é realizada usando JSON Web Tokens (JWT), garantindo que apenas usuários válidos possam acessar e modificar os dados.

## Tecnologias Utilizadas

- Django
- Django REST Framework
- djangorestframework-simplejwt
- SQLite (ou outro banco de dados de sua escolha)

## Estrutura do JWT

O JSON Web Token (JWT) é um padrão que define uma maneira compacta e autônoma de transmitir informações entre partes como um objeto JSON. O JWT é composto por três partes:

1. **Header (Cabeçalho)**: Contém informações sobre como o token é assinado.
2. **Payload (Carga Útil)**: Contém as declarações (claims) que são as informações que você deseja transmitir.
3. **Signature (Assinatura)**: Usada para verificar se o remetente do JWT é quem afirma ser e para garantir que a mensagem não foi alterada.

## Fluxo de Autenticação

1. O usuário fornece suas credenciais (nome de usuário e senha) para o servidor.
2. Se as credenciais forem válidas, o servidor gera um JWT e o envia de volta ao cliente.
3. O cliente armazena o token e o envia em cada requisição subsequente no cabeçalho `Authorization` como `Bearer <token>`.
4. O servidor valida o token em cada requisição para garantir que o usuário está autenticado.

## Endpoints

### 1. Registrar Usuário

- **Método**: `POST`
- **Endpoint**: `/api/registrar/`
- **Corpo da Requisição**:
    ```json
    {
        "username": "nome_do_usuario",
        "senha": "senha_do_usuario",
        "telefone": "telefone_do_usuario",
        "endereco": "endereco_do_usuario",
        "cpf": "cpf_do_usuario",
        "email": "email_do_usuario"
    }
    ```
- **Resposta**:
    - Sucesso: `201 Created`
    - Erro: `400 Bad Request`

### 2. Logar Usuário

- **Método**: `POST`
- **Endpoint**: `/api/logar/`
- **Corpo da Requisição**:
    ```json
    {
        "username": "nome_do_usuario",
        "senha": "senha_do_usuario"
    }
    ```
- **Resposta**:
    - Sucesso: `200 OK` com o token JWT
    - Erro: `401 Unauthorized`

### 3. Visualizar Dados do Usuário (Protegido)

- **Método**: `GET`
- **Endpoint**: `/api/view_protegida/`
- **Cabeçalho**:
    ```
    Authorization: Bearer <token>
    ```
- **Resposta**:
    - Sucesso: `200 OK`
    - Erro: `401 Unauthorized`

## Informações do Usuário

Cada usuário possui as seguintes informações:

- **Biografia**: Uma breve descrição sobre o usuário. [opcional]
- **Idade**: A idade do usuário. [opcional]
- **Telefone**: Um número de telefone de contato. [opcional]
- **Endereço**: O endereço físico do usuário. [opcional]
- **Escolaridade**: O nível de educação do usuário. [opcional]
- **Quantidade de Animais**: O número de animais de estimação que o usuário possui. [opcional]

- em meu caso as seguintes informações do usuário são:
- `obs` peguei este trecho da minha aplicação `views.py`
    **nome = request.data.get('username')**
    **senha = request.data.get('senha')**
    **telefone = request.data.get('telefone')**
    **endereco = request.data.get('endereco')**
    **cpf = request.data.get('cpf')**
    **email = request.data.get('email')**

## Configuração do Ambiente

Para configurar o ambiente, siga as instruções no guia de criação de ambiente:

[Criação de Ambiente] o passo a passo saira em breve...

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, faça um fork do repositório, crie uma nova branch e envie um pull request.
