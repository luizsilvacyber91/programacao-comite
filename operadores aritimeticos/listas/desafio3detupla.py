
tupla_com_repetidos = (1, 2, 2, 3, 4, 4, 5, 1)

print(f"Tupla original: {tupla_com_repetidos}")

elementos_unicos = set(tupla_com_repetidos)

print(f"Números únicos (em formato de conjunto): {elementos_unicos}")

tupla_unica = tuple(elementos_unicos)

print(f"Números únicos (em formato de tupla): {tupla_unica}")