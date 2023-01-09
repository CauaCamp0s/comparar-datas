### OQUE É UM API? -  é um lugar para disponibilizar recursos e funcionalidades 
### 1. QUAL O OBJETIVO? - Criar um api que disponibliza a consulta, criação
# , edição e exclusão de Pessoas.
### 2. URL base -  localhost
### 3. Endpoints - 
    # - localhost/livros (GET)  
    # - localhost/livros/id (GET)  
    # - localhost/livros/id (PUT)  
    # - localhost/livros/id (DELETE)  
# 4 - Quaisrecursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__) 
peoples = [
    {
        "id": 1,
        "name": "Luis Fonsi",
        "pais": "Nanci Santos  e Mario Rodrigues"
    },
    {
        "id": 2,
        "name": "Cauã Campos",
        "pais": "Jorge Marcos e Ivi Iris"
    },
    {
        "id": 3,
        "name": "Vinni Fárias",
        "pais": "Manoel Daniel e Carla Silva"
    },
    {
        "id": 4,
        "name": "Miguel Enzo",
        "pais": "Fábio e  Dayze"
    },
    {
        "id": 5,
        "name": "José Alves",
        "pais": "Eduardo e Bruna "
    },
    {
        "id": 6,
        "name": "Kaiky Vieira",
        "pais": "Marcos Jorge e Iris Ivis"
    }
]
# Consultar(todos)
@app.route('/peoples', methods=['GET'])
def obter_peoples():
    return jsonify(peoples)

# Consutar(id)
@app.route('/peoples/<int:id>', methods=['GET'])
def obter_people_id(id):
    for people in people:
        if people.get("id") == id:
            return jsonify(people)
    
# Editar
@app.route('/peoples/<int:id>', methods=['PUT'])
def edit_people_id(id):
    changed_people = request.get_json()
    for indece, people in enumerate(peoples):
        if people.get("id") == id:
            peoples[indece].update(changed_people)
            return jsonify(peoples[indece])
 
# Criar   

@app.route('/peoples/<int:id>', methods=['DELETE'])
def include_new_people():
    new_people = request.get_json()
    livros.append(new_people)
    
    return jsonify(peoples)

# Excluir

app.run(port=5000, host="localhost", debug=True)