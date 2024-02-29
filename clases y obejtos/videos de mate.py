from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Aquí puedes definir los datos de tus bloques de matemáticas como una lista de diccionarios o de la manera que prefieras
    data = {
        'primer_ano': [
            {
                'titulo': 'Bloque 1: Introducción a las Matemáticas',
                'descripcion': 'Introducción a las matemáticas para primer grado, cubriendo conceptos básicos como aprender a contar y números y operaciones: Identificación de números, contar, sumas y restas básicas.',
                'video_url': 'https://www.youtube.com/watch?v=klHsqsti6so'
            },
            {
                'titulo': 'Bloque 2: Figuras y Cuerpos Geométricos',
                'descripcion': 'Cómo enseñar contar, sumar y restar en primer grado de una manera sistemática y las figuras y cuerpos geométricos: Reconocimiento de formas simples como círculos, cuadrados y triángulos.',
                'video_url': 'https://www.youtube.com/watch?v=eirCSrVc0Q4'
            },
            # Añade más bloques según sea necesario
        ],
        # Define otros años aquí
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
