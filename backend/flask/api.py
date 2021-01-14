from apiks_flask_API import *

# route to get all movies
@app.route('/pet', methods=['GET'])
def get_pets():
    '''Function to get all the movies in the database'''
    return jsonify({'pet': pet.get_all_pets()})

# route to get movie by id
@app.route('/pet/<int:id>', methods=['GET'])
def get_pet_by_id(id):
    return_value = pet.get_pet(id)
    return jsonify(return_value)

# route to add new movie
@app.route('/pet', methods=['POST'])
def add_pet():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    pet.add_pet(request_data["pet_type_id"], request_data["name"],
                    request_data["client_id"], request_data["age"])
    response = Response("Pet added", 201, mimetype='application/json')
    return response

# route to delete movie using the DELETE method
@app.route('/pets/<int:id>', methods=['DELETE'])
def remove_pet(id):
    '''Function to delete movie from our database'''
    pet.delete_pet(id)
    response = Response("Movie Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)
