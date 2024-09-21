def syntax_analysis(token_list):
    structure_list = []

    for token in token_list:
        if token['valor'].lower() == 'for':  
            structure_list.append({
                'linea': token['linea'],
                'estructura': token['valor'],
                'valida': 'X',
                'error': ''
            })
        else:
            structure_list.append({
                'linea': token['linea'],
                'estructura': token['valor'],
                'valida': '',
                'error': 'X'
            })
    return structure_list