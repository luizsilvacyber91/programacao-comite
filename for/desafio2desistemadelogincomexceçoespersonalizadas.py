class UsuarioNaoEncontrado(Exception):
    """
    Exceção personalizada levantada quando um usuário não é encontrado.
    Herda de Exception, que é a classe base para a maioria das exceções integradas.
    """
    def __init__(self, usuario_digitado, mensagem="Usuário não encontrado"):
        self.usuario_digitado = usuario_digitado
        self.mensagem = mensagem
        super().__init__(self.mensagem)
    
    def __str__(self):
        return f'{self.mensagem}: "{self.usuario_digitado}"'

USUARIOS_DB = {
    "admin": "senha123",
    "joao": "abcde"
}

def fazer_login(username, password):
    """
    Função que tenta autenticar um usuário.
    Levanta UsuarioNaoEncontrado se o username não estiver no DB.
    """
    if username not in USUARIOS_DB:
        
        raise UsuarioNaoEncontrado(username)
    
    if USUARIOS_DB[username] == password:
        return True 
    else:
        return False 


try:
    
    usuario_inexistente = "pedro"
    senha_qualquer = "12345"
    print(f"Tentando logar com o usuário: {usuario_inexistente}")
    if fazer_login(usuario_inexistente, senha_qualquer):
        print(f"Login de {usuario_inexistente} bem-sucedido!")
except UsuarioNaoEncontrado as e:
    
    print(f"Erro ao tentar login: {e}")
    print(f"Detalhe: O usuário '{e.usuario_digitado}' não existe em nosso sistema.")

print("-" * 20)

try:
    
    usuario_existente = "admin"
    senha_correta = "senha123"
    print(f"Tentando logar com o usuário: {usuario_existente}")
    if fazer_login(usuario_existente, senha_correta):
        print(f"Login de {usuario_existente} bem-sucedido!")
except UsuarioNaoEncontrado as e:
    print(f"Erro ao tentar login: {e}")
