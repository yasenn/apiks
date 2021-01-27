#!/usr/bin/env python3

from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from flasgger import Swagger

app = Flask(__name__)
db = SQLAlchemy()
# Wrap the Api with swagger.docs. It is a thin wrapper around the Api class that adds some swagger smarts
# api = swagger.docs(Api(app), apiVersion='0.1')
swagger = Swagger(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'apiks.c8kflxch1q8h.eu-west-2.rds.amazonaws.com'
app.config['SQLALCHEMY_TRACK_MODFICATIONS'] = False

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/session_list", methods=['GET'])
def session_list():
    return jsonify({'Session_list': SessionList.get_all_session_lists()})

class SessionList(db.Model):
    __tablename__ = 'session_list'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    client_id = db.Column(db.Integer, nullable=False)
    # nullable is false so the column can't be empty
    clinic_id = db.Column(db.Integer, nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)
    price_list_id = db.Column(db.Integer, nullable=False)

    def __repr__(self,db):
        return 'USER %r' % self.db

    def json(self):
        return {'id': self.id, 'client_id': self.clinic_id,
                'clinic_id': self.clinic_id, 'doctor_id': self.doctor_id, 'date_of_visit': self.date_of_visit, 'price_list_id': self.price_list_id}

    def add_session_list(_client_id, _clinic_id, _doctor_id, _date_of_visit, _price_list_id):
        new_session_list = session_list(client_id=_client_id, clinic_id=_clinic_id, doctor_id=_doctor_id, date_of_visit=_date_of_visit, price_list_id=_price_list_id)
        db.session.add(new_session_list)
        db.session.commit()  # commit changes to session

class PriceList(db.Model):
    __tablename__ = 'price_list'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    service = db.Column(db.String(30), nullable=False)
    # nullable is false so the column can't be empty
    price = db.Column(db.Integer, nullable=False)
    doctor_position_id = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'id': self.id, 'service': self.service,
                'price': self.price, 'doctor_position_id': self.doctor_position_id}

class PetMedicalCard(db.Model):
    __tablename__ = 'pet_medical_card'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    doctor_id = db.Column(db.Integer, nullable=False)
    # nullable is false so the column can't be empty
    pet_id = db.Column(db.Integer, nullable=False)
    info = db.Column(db.String(1000), nullable=False)

    def json(self):
        return {'id': self.id, 'doctor_id': self.doctor_id,
                'pet_id': self.pet_id, 'info': self.info, 'date_of_visit': self.date_of_visit}

class Doctor(db.Model):
    __tablename__ = 'doctor'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(30), nullable=False)
    # nullable is false so the column can't be empty
    doctor_position_id = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    clinic_id = db.Column(db.Integer, nullable=False)
    cabinet = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name,
                'doctor_position_id': self.doctor_position_id, 'phone': self.phone, 'clinic_id': self.clinic_id, 'cabinet': self.cabinet}

class Clinic(db.Model):
    __tablename__ = 'clinic'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    address = db.Column(db.String(50), nullable=False)
    # nullable is false so the column can't be empty
    schedule_clinic = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def json(self):
        return {'id': self.id, 'address': self.address,
                'schedule_clinic': self.schedule_clinic, 'phone': self.phone}

class DoctorPosition(db.Model):
    __tablename__ = 'doctor_position'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    position = db.Column(db.String(20), nullable=False)
    # nullable is false so the column can't be empty

    def json(self):
        return {'id': self.id, 'position': self.position,}

class PetTable(db.Model):
    __tablename__ = 'Pet'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    pet_type_id = db.Column(db.Integer, nullable=False)
    # nullable is false so the column can't be empty
    name = db.Column(db.String(30), nullable=False)
    client_id = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'id': self.id, 'pet_type_id': self.pet_type_id,
                'name': self.name, 'client_id': self.client_id, 'age': self.age}

    def add_pet(_pet_type_id, _name, _client_id, _age):
        request_data = request.get_json()  # getting data from client
        pet.add_pet(request_data["pet_type_id"], request_data["name"],
            request_data["client_id"], request_data["age"])
        response = Response("Pet added", 201, mimetype='application/json')
        new_pet = PetTable(pet_type_id=_pet_type_id, name=_name, client_id=_client_id, age=_age)
        db.session.commit()  # commit changes to session
        return response

    def get_all_pets():
        return [PetTable.json(pet) for pet in PetTable.query.all()]

    def get_pet(_name):
        return [PetTable.json(PetTable.query.filter_by(name=_name).first())]

class Client(db.Model):
    __tablename__ = 'client'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(30), nullable=False)
    # nullable is false so the column can't be empty
    phone = db.Column(db.String(13), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    user_role_id = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name,
                'phone': self.phone, 'email': self.email, 'user_role': self.user_role}

class UserRole(db.Model):
    __tablename__ = 'user_role'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    role = db.Column(db.String(15), nullable=False)
    # nullable is false so the column can't be empty

    def json(self):
        return {'id': self.id, 'role': self.role}

class PetType(db.Model):
    __tablename__ = 'pet_type'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    type = db.Column(db.String(30), nullable=False)
    # nullable is false so the column can't be empty

    def json(self):
        return {'id': self.id, 'type': self.type}

#@app.route('/pet', methods=['GET'])
#def get_pets():
#    return jsonify({'pet': PetTable.get_all_pets()})

@app.route('/pet/<int:id>', methods=['GET'])
def get_pet_by_id(id):
    """Example endpoint returning a pet by it's id
    This is using docstrings for specifications.
    ---
    parameters:
      - name: Pet't id
        in: path
        type: string
        required: true
    responses:
      200:
        description: Information about the pet
    """
    return_value = PetTable.get_pet(id)
    return jsonify(return_value)

@app.route('/pet', methods=['POST'])
def add_pet():
    """Example endpoint adding a new pet to the list of pets
    This is using docstrings for specifications.
    ---
    parameters:
      - name: Pet's id
        in: path
        type: Integer
        required: true
        description: Type down the id of new pet
      - name: name
        in: path
        type: string
        required: true
        description: Name of the pet required
      - name: client id
        in: path
        type: Integer
        required: true
        description: Client id
      - name: age
        in: path
        type: Integer
        required: true
        description: Age of the pet
    responses:
      200:
        description: New pet was added
    """
    request_data = request.get_json()  # getting data from client
    pet.add_pet(request_data["pet_type_id"], request_data["name"],
                    request_data["client_id"], request_data["age"])
    response = Response("Pet added", 201, mimetype='application/json')
    return response

@app.route('/pets/<int:id>', methods=['DELETE'])
def remove_pet(id):
    """Example endpoint deleting a pet by it's id
    This is using docstrings for specifications.
    ---
    parameters:
      - name: Delete pet by it's id
        in: path
        type: string
        description: pet's id
        required: true
        default: all
    responses:
      200:
        description: Pet was deleted
    """
    pet.delete_pet(id)
    response = Response("Pet Deleted", status=200, mimetype='application/json')
    return response

@app.route('/pet', methods=['GET'])
def get_pets():
    """Example endpoint returning a list of pets
    This is using docstrings for specifications.
    ---
    parameters:
      - name: Pets
        in: path
        type: string
        enum: ['all', 'cats', 'dogs']
        required: true
        default: all
    definitions:
      Pets:
        type: object
        properties:
          pet_name:
            type: array
            items:
              $ref: '#/pet'
      Pet:
        type: string
    responses:
      200:
        description: A list of pets (may be filtered by type)
        schema:
          $ref: '#/pet'
        examples:
          rgb: ['name1', 'name2', 'name3']
    """
#    all_colors = {
#        'cmyk': ['cian', 'magenta', 'yellow', 'black'],
#        'rgb': ['red', 'green', 'blue']
#    }
    return jsonify({'pet': PetTable.get_all_pets()})

if __name__ == "__main__":
    app.run(port=5432, debug=True)
