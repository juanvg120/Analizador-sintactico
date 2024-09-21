from flask import Flask, render_template, request
from lexer import lexer  # Importamos el lexer
from parser import syntax_analysis  # Importamos el parser

app = Flask(__name__)

# Ruta principal de la aplicación
@app.route('/', methods=['GET', 'POST'])
def home():
    tokens = []
    structures = []

    if request.method == 'POST':
        code = request.form['codigo']
        
        # Análisis léxico
        tokens = lexer(code)
        
        # Análisis sintáctico
        structures = syntax_analysis(tokens)

    return render_template('index.html', tokens=tokens, structures=structures)

if __name__ == '__main__':
    app.run(debug=True)
