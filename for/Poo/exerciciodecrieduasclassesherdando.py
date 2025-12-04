class Animal:
    """Classe base para representar um animal."""
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        """Método comum que será sobrescrito pelas subclasses."""
        print("O animal está fazendo um som genérico.")

class Cachorro(Animal):
    
    def emitir_som(self):
        
        print(f"O cachorro {self.nome} está latindo: Au Au!")
    
    def buscar(self):
        
        print(f"O cachorro {self.nome} está buscando a bolinha.")

class Gato(Animal):
    
    def emitir_som(self):
        
        print(f"O gato {self.nome} está miando: Miau!")

    def arranhar(self):
        
        print(f"O gato {self.nome} está arranhando o sofá.")

meu_cachorro = Cachorro(nome="Buddy")
meu_gato = Gato(nome="Felix")

meu_cachorro.emitir_som() 
meu_cachorro.buscar()    

meu_gato.emitir_som()    
meu_gato.arranhar()      

def fazer_som_animal(animal):
    animal.emitir_som()

print("\nDemonstração de polimorfismo:")
fazer_som_animal(meu_cachorro) 
fazer_som_animal(meu_gato)     