#!/usr/bin/env python3

from settings import *
import json
from myapp import api

db = SQLAlchemy(app)

class Session_list(db.Model):
    __tablename__ = 'Session_list'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    client_id = db.Column(db.Integer, nullable=False)
    # nullable is false so the column can't be empty
    clinic_id = db.Column(db.Integer, nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)
    date_of_visit = db.Column(db.date_time_obj, nullable=False)
    price_list_id = db.Column(db.Integer, nullable=False)


# You may decorate your operation with @swagger.operation
class Session_list(db.Model):
    "get_session_list"
    @swagger.operation(
        notes='Get list of sessions',
        responseClass=ModelClass.__name__,
        nickname='session_list',
        parameters=[ ],
        responseMessages=[
            {
              "code": 200,
              "message": "List of sessions"
            },
            {
              "code": 405,
              "message": "Invalid input"
            },
            {
              "code": 503,
              "message": "Server error"
            }
          ]
        )
    def json(self):
        return {'id': self.id, 'client_id': self.clinic_id,
                'clinic_id': self.clinic_id, 'doctor_id': self.doctor_id, 'date_of_visit': self.date_of_visit, 'price_list_id': self.price_list_id}

    def add_session_list(_client_id, _clinic_id, _doctor_id, _date_of_visit, _price_list_id):
        '''function to add movie to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our Movie constructor
        new_session_list = session_list(client_id=_client_id, clinic_id=_clinic_id, doctor_id=_doctor_id, date_of_visit=_date_of_visit, price_list_id=_price_list_id)
        db.session.add(new_session_list)  # add new movie to database session
        db.session.commit()  # commit changes to session

class Price_list(db.Model):
    "get price list"
    @swagger.operation(
        notes='Get price list ',
        responseClass=ModelClass.__name__,
        nickname='session_list',
        parameters=[ ],
        responseMessages=[
            {
              "code": 200,
              "message": "Price List "
            },
            {
              "code": 405,
              "message": "Invalid input"
            },
            {
              "code": 503,
              "message": "Server error"
            }
          ]
        )
    __tablename__ = 'Price_list'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    service = db.Column(db.String(30), nullable=False)
    # nullable is false so the column can't be empty
    price = db.Column(db.Integer, nullable=False)
    doctor_position_id = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'id': self.id, 'service': self.service,
                'price': self.price, 'doctor_position_id': self.doctor_position_id}

class Pet_medical_card(db.Model):
    "get_session_list"
    @swagger.operation(
        notes='Get list of sessions',
        responseClass=ModelClass.__name__,
        nickname='session_list',
        parameters=[ ],
        responseMessages=[
            {
              "code": 200,
              "message": "List of sessions"
            },
            {
              "code": 405,
              "message": "Invalid input"
            },
            {
              "code": 503,
              "message": "Server error"
            }
          ]
        )
    __tablename__ = 'Pet_medical_card'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    doctor_id = db.Column(db.Integer, nullable=False)
    # nullable is false so the column can't be empty
    pet_id = db.Column(db.Integer, nullable=False)
    info = db.Column(db.String(1000), nullable=False)
    date_of_visit = db.Column(db.date_time_obj, nullable=False)

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

class Doctor_position(db.Model):
    __tablename__ = 'doctor_position'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    position = db.Column(db.String(20), nullable=False)
    # nullable is false so the column can't be empty

    def json(self):
        return {'id': self.id, 'position': self.position,}

class Pet(db.Model):
    __tablename__ = 'pet'  # creating a table name
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
        '''function to add movie to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our Movie constructor
        new_pet = Movie(pet_type_id=_pet_type_id, name=_name, client_id=_client_id, age=_age)
        db.session.add(new_pet)  # add new movie to database session
        db.session.commit()  # commit changes to session

    def get_all_pets():
        '''function to get all movies in our database'''
        return [pet.json(pet) for pet in pet.query.all()]

    def get_pet(_name):
        '''function to get movie using the id of the movie as parameter'''
        return [pet.json(pet.query.filter_by(name=_name).first())]
        # Movie.json() coverts our output to the json format defined earlier
        # the filter_by method filters the query by the id
        # since our id is unique we will only get one result
        # the .first() method will get that first value returned

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

class User_role(db.Model):
    __tablename__ = 'user_role'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    role = db.Column(db.String(15), nullable=False)
    # nullable is false so the column can't be empty

    def json(self):
        return {'id': self.id, 'role': self.role}

class Pet_type(db.Model):
    __tablename__ = 'pet_type'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    type = db.Column(db.String(30), nullable=False)
    # nullable is false so the column can't be empty

    def json(self):
        return {'id': self.id, 'type': self.type}
