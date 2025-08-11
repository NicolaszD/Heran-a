# Classe Livro
class Livro:
    def __init__(self, titulo, autor, editora):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora

    def display_details(self): #Mostar detalhes
        print(f"O livro: {self.titulo}, do(a) autor(a): {self.autor}, da editora: {self.editora}.")

# Classe Revista
class Revista:
    def __init__(self, titulo, autor, editora):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora

    def display_details(self):  #Mostar detalhes
        print(f"A revista: {self.titulo}, do(a) autor(a): {self.autor}, da editora: {self.editora}.")

# Classe jornal
class Jornal:
    def __init__(self, titulo, autor, editora):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora

    def display_details(self):  #Mostar detalhes
        print(f"O jornal: {self.titulo}, do(a) autor(a): {self.autor}, da editora: {self.editora}.")

# Imprimir livro e detalhes
livro = Livro("Harry Potter", "Nicolas", "Brasil")
livro.display_details()

# Imprimir Revista e detalhes
revista = Revista("Futebol", "Nicolas", "Brasileira")
revista.display_details()

# Imprimir Jornal e detalhes
jornal = Jornal("Globo", "Nicolas", "Brasuca")
jornal.display_details()