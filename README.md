<h1 align="center" style="font-weight: bold;">agenda-Flask-Angular 💻</h1>

<p align="center">
 <a href="#tech">Tecnologias</a> • 
 <a href="#started">Se preparando</a> •
 <a href="#routes">APP Routes</a> • 
 <a href="#colab">Colaboladores</a> •
 <a href="#contribute">Contribua</a>
</p>

<p align="center">
    <b>Por enquanto, apenas uma API para CRUD de contatos de uma agenda com autenticação </b>
</p>

<h2 id="technologies">💻 Tecnologias</h2>

- Flask

<h2 id="started">🚀 Se preparando</h2>

Para rodar a API siga os seguintes passos

<h3>Prerequisites</h3>


- [PYTHON](https://www.python.org/downloads/)
- [FLASK](https://flask.palletsprojects.com/en/2.3.x/)

<h3>Cloning</h3>

Para clonar basta rodar

```bash
git clone https://github.com/LimeHawk/agenda-Flask-Angular.git
```

<h3>Starting</h3>

Para começar siga esses Passos:

```bash
cd agenda-Flask-Angular
cd BackEnd
```
Crie um .env com as seguintes informações e salve na raiz do projeto:

```bash
DATABASE_NAME = "./app/database/agenda.db"
LOGINACESS = "seu_login"
PASSWORD ="sua_senha"
JWT_ENCRYPTION_KEY = "sua_chave"
```

Windows


```bash
pip install -r requirements.txt
cd  app/database
python create_database.py
cd .. 
cd .. 
python main.py
```

Ubuntu

```bash
cd agenda-Flask-Angular
cd BackEnd
pip install -r requirements.txt
cd  app/database
python3 create_database.py
cd .. 
cd .. 
python3 main.py
```

<h2 id="routes">📍 Application Routes</h2>

Para ter acesso a outras funções primeiro você precisa ter o token.

Como você estará rodando localmente todas as saidas estarão na http://127.0.0.1:5000
​
| route               | request    | response                                        
|----------------------|-----------------------------------------------------|---------------------------
| <kbd>POST /api/v1/login</kbd>   | `json` with `email` and `senha`| `json` `access_token`
| <kbd>Get /api/v1/contato</kbd>  | None | Lista de contatos no BD
| <kbd>POST /api/v1/contato</kbd> | `json` with `nome` and `email` and `telefone`| `json` `message`
| <kbd>PUT /api/v1/contato</kbd>  | `json` with `nome` and `email` and `telefone` and `id`| `json` `message`
| <kbd>DELETE /api/v1/contato/<string:id></kbd> | None | `json` `message`



<h2 id="colab">🤝 Collaborators</h2>

Special thank you for all people that contributed for this project.

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/96706378?s=400&u=c9ec291bbbb7ff2f92b39ba6350b6eb6894e7036&v=4" width="100px;" alt="Kaike Profile Picture"/><br>
        <sub>
          <b>Kaíke Falcão</b>
        </sub>
      </a>
    </td>
    
  </tr>
</table>

<h2 id="contribute">📫 Contribute</h2>

Apenas seguir os passos abaixo para contribuir, será de enorme ajuda

1. `git clone https://github.com/LimeHawk/agenda-Flask-Angular.git`
2. `git checkout -b feature/NAME`
3. Follow commit patterns
4. Open a Pull Request explaining the problem solved or feature made, if exists, append screenshot of visual modifications and wait for the review!

<h3>Documentations that might help</h3>

[📝 How to create a Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

[💾 Commit pattern](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)
