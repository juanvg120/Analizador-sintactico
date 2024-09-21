import re

# Definición de palabras clave reservadas
keywords = {"for": "Palabra reservada"}

# Función para analizar el código y extraer los tokens
def lexer(code):
    token_list = []
    lines = code.splitlines()

    # Análisis línea por línea
    for line_num, line in enumerate(lines, start=1):
        for match in re.finditer(r'\b\w+\b', line):
            word = match.group(0)
            # Identificación de tipo de palabra (reservada o identificador)
            if word.lower() in keywords:
                token_type = "Palabra reservada"
            else:
                token_type = "Identificador"
            token_list.append({
                'tipo': token_type,
                'valor': word,
                'linea': line_num,
                'columna': match.start() + 1
            })
    return token_list