from flask import Flask, request, jsonify, render_template
from ibm_watsonx_ai.foundation_models import Model
import os
app = Flask(__name__)
def get_credentials():
    return {
        "url": "https://us-south.ml.cloud.ibm.com",
        "apikey": ""
    }
# Configura el modelo
model_id =  "ibm/granite-13b-chat-v2"
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 500,
    "repetition_penalty": 1
}
project_id = os.getenv("PROJECT_ID", "")
# Inicializamos el modelo
try:
    print("Iniciando el modelo...")
    model = Model(
        model_id=model_id,
        params=parameters,
        credentials=get_credentials(),
        project_id=project_id
    )
    print("Modelo inicializado correctamente.")
except Exception as e:
    print(f"Error al inicializar el modelo: {e}")

prompt_contexto = """Voy a analizar tu negocio en profundidad, incluyendo fortalezas, debilidades, competidores, alcance y recomendaciones con respecto al mercado existente. Aquí está cómo voy a abordar este análisis:

Fortalezas de tu negocio con respecto al mercado existente:

Primero, identificaré las ventajas internas de tu negocio en comparación con el mercado actual. Evaluaré qué aspectos de tu propuesta te hacen destacar entre las ofertas existentes. Si tu negocio tiene características únicas o recursos valiosos, los destacaré.
Debilidades con respecto al mercado existente:

Luego, analizaré las posibles debilidades internas de tu negocio en comparación con las expectativas y estándares del mercado. Identificaré áreas que podrían representar desafíos o limitaciones, como costos elevados o falta de recursos específicos.
Competidores con respecto al mercado existente:

A continuación, examinaré el panorama competitivo en tu sector. Identificaré quiénes son tus principales competidores y qué ventajas o características tienen en el mercado. Esto te ayudará a situar tu negocio en el contexto de la competencia actual.
Alcance con respecto al mercado existente:

Evaluaré el alcance potencial de tu negocio en el mercado. Esto incluye el tamaño del mercado y las oportunidades de crecimiento que puedes aprovechar. Analizaré cómo tu negocio puede posicionarse para captar una parte significativa del mercado.
Recomendaciones con respecto al mercado existente:

Finalmente, proporcionaré recomendaciones basadas en el análisis anterior. Ofreceré sugerencias para mejorar tus fortalezas, abordar debilidades, competir eficazmente y expandir mi alcance en el mercado.
Todo esto en un maximo de 300 caracteres, tu idea de negocio es :
"""
print('Se termino de evaluar el prompt')
# Ruta para el frontend
@app.route('/')
def home():
    return render_template('index.html')
print('se evaluo la ruta del index')
# Ruta para procesar el input del usuario y generar la respuesta
@app.route('/generate', methods=['POST'])
def generate_text():
    prompt_input = request.json.get('input')
    prompt_casi_listo=prompt_input+(" mi analisis es:")
    final_input=prompt_contexto+prompt_casi_listo
    try:
        generated_response = model.generate_text(prompt=final_input, guardrails=False)
        return jsonify({"response": generated_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def format_response(response_text):
    # Divide la respuesta en secciones
    sections = response_text.split('\n\n')
    formatted_sections = []

    section_titles = ['Fortaleza', 'Debilidades', 'Competidores', 'Alcance', 'Recomendaciones']

    for i, section in enumerate(sections):
        if i < len(section_titles):
            formatted_sections.append(f"{section_titles[i]}:\n{section.strip()}")

    return "\n\n".join(formatted_sections)
if __name__ == '__main__':
    app.run(debug=True)



