    CREATE TABLE pet_type (
		id SERIAL PRIMARY KEY,
		type VARCHAR (30) UNIQUE NOT NULL
	);

	CREATE TABLE doctor_position (
		id SERIAL PRIMARY KEY,
		position VARCHAR (20) UNIQUE NOT NULL
	);

	CREATE TABLE price_list (
		id SERIAL PRIMARY KEY,
		service VARCHAR (30) UNIQUE,
		price SMALLINT NOT NULL,
		doctor_position_id SMALLINT NOT NULL
	);

	CREATE TABLE clinic (
		id SERIAL PRIMARY KEY,
		address VARCHAR (50) UNIQUE NOT NULL,
		schedule_clinic VARCHAR (20) NOT NULL,
		phone VARCHAR (20) UNIQUE NOT NULL
	);

	CREATE TABLE user_role (
		id SERIAL PRIMARY KEY,
		role VARCHAR (15)
	);

	CREATE TABLE doctor (
		id SERIAL PRIMARY KEY,
		name VARCHAR(30) NOT NULL,
		doctor_position_id SMALLINT NOT NULL,
		phone VARCHAR(13) UNIQUE,
		clinic_id SMALLINT NOT NULL,
		cabinet SMALLINT NOT NULL
	);

	CREATE TABLE client (
		id SERIAL PRIMARY KEY,
		name VARCHAR (30) NOT NULL,
		phone VARCHAR(13) NOT NULL,
		email VARCHAR(30),
		user_role_id SMALLINT NOT NULL
	);

	CREATE TABLE pet (
		id SERIAL PRIMARY KEY,
		pet_type_id SMALLINT NOT NULL,
		name VARCHAR(30) NOT NULL,
		client_id SMALLINT NOT NULL,
		age SMALLINT
	);

	CREATE TABLE pet_medical_card (
		id SERIAL PRIMARY KEY,
		doctor_id SMALLINT NOT NULL,
		pet_id SMALLINT NOT NULL,
		info VARCHAR (1000),
		date_of_visit DATE NOT NULL
	);

	CREATE TABLE session_list (
		id SERIAL PRIMARY KEY,
		client_id SMALLINT NOT NULL,
		clinic_id SMALLINT NOT NULL,
		doctor_id SMALLINT NOT NULL,
		date_of_visit DATE NOT NULL,
		price_list_id SMALLINT NOT NULL
	);

alter TABLE session_list add constraint fk_session_doctor_id FOREIGN KEY (doctor_id) REFERENCES  doctor (id);
alter TABLE session_list add constraint fk_client_id FOREIGN KEY (client_id) REFERENCES  client (id);
alter TABLE session_list add constraint fk_price_list_id FOREIGN KEY (price_list_id) REFERENCES  price_list (id);
alter TABLE session_list add constraint fk_clinic_id FOREIGN KEY (clinic_id) REFERENCES clinic (id);

alter TABLE price_list add constraint fk_price_doctor_position_id FOREIGN KEY (doctor_position_id) REFERENCES doctor_position(id);

alter TABLE client add constraint fk_user_role_id FOREIGN KEY (user_role_id) REFERENCES user_role(id);

alter TABLE pet add constraint fk_pet_type_id FOREIGN KEY (pet_type_id) REFERENCES pet_type(id);
alter TABLE pet add constraint fk_pet_client_id FOREIGN KEY (client_id) REFERENCES client(id);

alter TABLE doctor add constraint fk_doctor_position_id FOREIGN KEY (doctor_position_id) REFERENCES doctor_position(id);
alter TABLE doctor add constraint fk_doctor_clinic_id FOREIGN KEY (clinic_id) REFERENCES clinic(id);

alter TABLE pet_medical_card add constraint fk_pet_id FOREIGN KEY (pet_id) REFERENCES pet(id);
alter TABLE pet_medical_card add constraint fk_doctor_id FOREIGN KEY (doctor_id) REFERENCES doctor(id);

