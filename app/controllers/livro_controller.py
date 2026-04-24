from flask import Blueprint, render_template, request, redirect, url_for
from app.models.livro_model import livro_model

livro_bp = Blueprint("livro_bp", __name__)


@livro_bp.route("/")
def index():
    termo = request.args.get("q", "").strip()
    livros = livro_model.pesquisar(termo)
    return render_template("index.html", livros=livros, termo=termo)


@livro_bp.route("/catalogo")
def catalogo():
    livros = livro_model.listar_todos()
    return render_template("catalogo.html", livros=livros)


@livro_bp.route("/livro/<int:livro_id>")
def detalhes_livro(livro_id):
    livro = livro_model.buscar_por_id(livro_id)

    if livro is None:
        return "Livro não encontrado.", 404

    return render_template("livro.html", livro=livro)


@livro_bp.route("/novo", methods=["GET", "POST"])
def novo_livro():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        autor = request.form.get("autor", "").strip()
        categoria = request.form.get("categoria", "").strip()
        ano = request.form.get("ano", "").strip()
        resumo = request.form.get("resumo", "").strip()
        disponivel = request.form.get("disponivel") == "on"

        if not titulo or not autor or not categoria or not ano:
            return "Erro: preencha todos os campos obrigatórios.", 400

        try:
            ano = int(ano)
        except ValueError:
            return "Erro: o ano precisa ser um número inteiro.", 400

        livro_model.adicionar(
            titulo=titulo,
            autor=autor,
            categoria=categoria,
            ano=ano,
            resumo=resumo,
            disponivel=disponivel,
        )
        return redirect(url_for("livro_bp.catalogo"))

    return render_template("novo_livro.html")


@livro_bp.route("/excluir/<int:livro_id>", methods=["POST"])
def excluir_livro(livro_id):
    livro_model.excluir(livro_id)
    return redirect(url_for("livro_bp.catalogo"))
