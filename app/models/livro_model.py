class LivroModel:
    def __init__(self):
        self._livros = [
            {
                "id": 1,
                "titulo": "Dom Casmurro",
                "autor": "Machado de Assis",
                "categoria": "Romance",
                "ano": 1899,
                "disponivel": True,
                "resumo": "Clássico da literatura brasileira que acompanha a história de Bentinho e Capitu."
            },
            {
                "id": 2,
                "titulo": "O Pequeno Príncipe",
                "autor": "Antoine de Saint-Exupéry",
                "categoria": "Fábula",
                "ano": 1943,
                "disponivel": True,
                "resumo": "Uma obra sobre amizade, amor, infância e o verdadeiro valor das coisas."
            },
            {
                "id": 3,
                "titulo": "1984",
                "autor": "George Orwell",
                "categoria": "Distopia",
                "ano": 1949,
                "disponivel": False,
                "resumo": "Romance distópico sobre vigilância extrema, manipulação e autoritarismo."
            },
            {
                "id": 4,
                "titulo": "Clean Code",
                "autor": "Robert C. Martin",
                "categoria": "Tecnologia",
                "ano": 2008,
                "disponivel": True,
                "resumo": "Livro sobre boas práticas para escrever código limpo e de fácil manutenção."
            }
        ]

    def listar_todos(self):
        return self._livros

    def listar_destaques(self, limite=4):
        return self._livros[:limite]

    def buscar_por_id(self, livro_id):
        for livro in self._livros:
            if livro["id"] == livro_id:
                return livro
        return None

    def pesquisar(self, termo):
        termo = termo.strip().lower()

        if not termo:
            return self.listar_destaques()

        resultados = []
        for livro in self._livros:
            if (
                termo in livro["titulo"].lower()
                or termo in livro["autor"].lower()
                or termo in livro["categoria"].lower()
            ):
                resultados.append(livro)

        return resultados

    def gerar_novo_id(self):
        if not self._livros:
            return 1
        return max(livro["id"] for livro in self._livros) + 1

    def adicionar(self, titulo, autor, categoria, ano, resumo, disponivel):
        novo_livro = {
            "id": self.gerar_novo_id(),
            "titulo": titulo,
            "autor": autor,
            "categoria": categoria,
            "ano": ano,
            "disponivel": disponivel,
            "resumo": resumo,
        }
        self._livros.append(novo_livro)
        return novo_livro

    def excluir(self, livro_id):
        livro = self.buscar_por_id(livro_id)
        if livro:
            self._livros.remove(livro)
            return True
        return False


livro_model = LivroModel()
