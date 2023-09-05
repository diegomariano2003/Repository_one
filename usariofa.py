from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ler_json', methods=['GET'])
def ler_json():
    try:
        # Lê o arquivo JSON
        with open('dados.json', 'r') as file:
            data = file.read()
        
        # Converte o JSON em um dicionário
        json_data = json.loads(data)

        return jsonify(json_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
                                                                                  

