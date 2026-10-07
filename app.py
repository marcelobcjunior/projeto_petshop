from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'chave-dev-petshop'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///petshop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    celular = db.Column(db.String(30))
    data_nascimento = db.Column(db.String(10))
    cpf = db.Column(db.String(14))
    nivel_acesso = db.Column(db.String(30), nullable=False)
    cep = db.Column(db.String(9))
    endereco = db.Column(db.String(150))
    numero = db.Column(db.String(20))
    complemento = db.Column(db.String(100))
    cidade = db.Column(db.String(80))
    estado = db.Column(db.String(2))


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    categoria = db.Column(db.String(80), nullable=False)
    marca = db.Column(db.String(80))
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    fornecedor = db.Column(db.String(120))


class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(255))
    preco = db.Column(db.Float, nullable=False)
    duracao = db.Column(db.Integer, nullable=False)
    responsavel = db.Column(db.String(120))


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template(
        "index.html",
        total_usuarios=Usuario.query.count(),
        total_produtos=Produto.query.count(),
        total_servicos=Servico.query.count(),
    )


@app.route("/sem-menu")
def sem_menu():
    return render_template("sem_menu.html")


@app.route("/usuarios")
def listar_usuarios():
    usuarios = Usuario.query.order_by(Usuario.id.desc()).all()
    return render_template("usuarios/listar.html", usuarios=usuarios)


@app.route("/usuarios/cadastrar", methods=["GET", "POST"])
def cadastrar_usuario():
    if request.method == "POST":
        usuario = Usuario(
            nome=request.form["nome"],
            email=request.form["email"],
            celular=request.form.get("celular"),
            data_nascimento=request.form.get("data_nascimento"),
            cpf=request.form.get("cpf"),
            nivel_acesso=request.form["nivel_acesso"],
            cep=request.form.get("cep"),
            endereco=request.form.get("endereco"),
            numero=request.form.get("numero"),
            complemento=request.form.get("complemento"),
            cidade=request.form.get("cidade"),
            estado=request.form.get("estado"),
        )
        db.session.add(usuario)
        db.session.commit()
        flash("Usuário cadastrado com sucesso!", "success")
        return redirect(url_for("listar_usuarios"))
    return render_template("usuarios/cadastrar.html")


@app.route("/produtos")
def listar_produtos():
    produtos = Produto.query.order_by(Produto.id.desc()).all()
    return render_template("produtos/listar.html", produtos=produtos)


@app.route("/produtos/cadastrar", methods=["GET", "POST"])
def cadastrar_produto():
    if request.method == "POST":
        produto = Produto(
            nome=request.form["nome"],
            categoria=request.form["categoria"],
            marca=request.form.get("marca"),
            preco=float(request.form["preco"]),
            estoque=int(request.form["estoque"]),
            fornecedor=request.form.get("fornecedor"),
        )
        db.session.add(produto)
        db.session.commit()
        flash("Produto cadastrado com sucesso!", "success")
        return redirect(url_for("listar_produtos"))
    return render_template("produtos/cadastrar.html")


@app.route("/servicos")
def listar_servicos():
    servicos = Servico.query.order_by(Servico.id.desc()).all()
    return render_template("servicos/listar.html", servicos=servicos)


@app.route("/servicos/cadastrar", methods=["GET", "POST"])
def cadastrar_servico():
    if request.method == "POST":
        servico = Servico(
            nome=request.form["nome"],
            descricao=request.form.get("descricao"),
            preco=float(request.form["preco"]),
            duracao=int(request.form["duracao"]),
            responsavel=request.form.get("responsavel"),
        )
        db.session.add(servico)
        db.session.commit()
        flash("Serviço cadastrado com sucesso!", "success")
        return redirect(url_for("listar_servicos"))
    return render_template("servicos/cadastrar.html")


if __name__ == "__main__":
    app.run(debug=True)