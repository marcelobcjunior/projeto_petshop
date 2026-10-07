# PetShop Manager — Projeto Flask

Projeto acadêmico desenvolvido para a disciplina de desenvolvimento web com Flask.

## Tema
Sistema de gerenciamento de um Pet Shop.

O sistema possui três tabelas principais:
- Usuários
- Produtos
- Serviços

## Requisitos
- Python 3.10+
- Git

## Instalação no Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Se o PowerShell bloquear o `Activate.ps1`, use:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe app.py
```

Acesse:
http://127.0.0.1:5000

## Git

```bash
git init
git add .
git commit -m "Projeto inicial Flask PetShop"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/flask-petshop.git
git push -u origin main
```

## Rotas

- `/` — página inicial
- `/sem-menu` — exemplo de template sem menu
- `/usuarios` — listar usuários
- `/usuarios/cadastrar` — cadastrar usuário
- `/produtos` — listar produtos
- `/produtos/cadastrar` — cadastrar produto
- `/servicos` — listar serviços
- `/servicos/cadastrar` — cadastrar serviço
