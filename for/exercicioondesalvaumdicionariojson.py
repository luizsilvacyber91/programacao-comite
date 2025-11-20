import json

dados_para_salvar = {
    "nome": "Fulano",
    "idade": 30,
    "cidade": "São Paulo",
    "habilidades": ["Python", "JSON", "Programação"],
    "ativo": True
}

nome_do_arquivo = "dados_usuario.json"

try:
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados_para_salvar, arquivo, ensure_ascii=False, indent=4)
    print(f"Dicionário salvo com sucesso em '{nome_do_arquivo}'")

except IOError as e:
    print(f"Erro ao salvar o arquivo: {e}")
          
try:
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
        dados_carregados = json.load(arquivo)
    print("\nConteúdo do arquivo lido de volta:")
    print(dados_carregados)
except IOError as e:
    print(f"Erro ao carregar o arquivo: {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON: {e}")