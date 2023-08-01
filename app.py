from flask import Flask, render_template, send_from_directory
import os


app = Flask(__name__)

# Dados fictícios dos projetos
projetos = [
    {
        'titulo': 'Projeto 1',
        'descricao': 'Descrição do Projeto 1...',
        'imagem': 'projeto1.jpg'
    },
    {
        'titulo': 'Projeto 2',
        'descricao': 'Descrição do Projeto 2...',
        'imagem': 'projeto2.jpg'
    },
    {
        'titulo': 'Projeto 3',
        'descricao': 'Descrição do Projeto 3...',
        'imagem': 'projeto3.jpg'
    }
]

@app.route('/images/<path:filename>')
def serve_image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, 'images'), filename)

@app.route('/')
def index():
    return render_template('index.html', projetos=projetos)

@app.route('/project/<int:id>')
def project(id):
    projeto = projetos[id]
    return render_template('project.html', projeto=projeto)

if __name__ == '__main__':
    app.run(debug=True)
