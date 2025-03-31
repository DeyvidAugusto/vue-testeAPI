from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Carregando CSV
def carregar_csv():
    return pd.read_csv('python-server/relatorio.csv', sep=';', on_bad_lines='skip')

@app.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('q', '').lower() 
    df = carregar_csv()
    
    resultados = df[df.apply(lambda row: query in row.astype(str).str.lower().values, axis=1)]
    
    return resultados.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)