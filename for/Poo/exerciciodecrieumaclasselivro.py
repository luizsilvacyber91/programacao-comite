class Livro:
    def __init__(self, titulo, autor):
        
        self.titulo = titulo
        self.autor = autor

    def exibir_info(self):
        
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")

livro1 = Livro("Dom Quixote", "Miguel de Cervantes")

livro1.exibir_info()
