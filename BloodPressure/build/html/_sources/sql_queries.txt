SQL Queries
=============================
Mysql
-----------------------------
CREATE TABLE person (
		id_person INT PRIMARY KEY AUTO_INCREMENT,
		first_name VARCHAR(45),
		last_name VARCHAR(45),
		middle_name VARCHAR(45),
		age INT,
		weight FLOAT,
		height INT,
		phone_number VARCHAR(45));

CREATE TABLE doctor (
		id_doctor INTEGER PRIMARY KEY AUTO_INCREMENT,
		first_name VARCHAR(45),
		last_name VARCHAR(45),
		middle_name VARCHAR(45),
		profession VARCHAR(45),
		phone_number VARCHAR(45));

CREATE TABLE pressure_data (
		id_pressure_data INT PRIMARY KEY AUTO_INCREMENT,
		date DATE,
		time TIME,
		upper_level INT,
		lower_level INT,
		pulse INT,
		person_id_person INT,
		doctor_id_doctor INT,
		FOREIGN KEY(person_id_person) REFERENCES person(id_person),
		FOREIGN KEY(doctor_id_doctor) REFERENCES doctor(id_doctor));

SQLite
-----------------------------
CREATE TABLE person (
    "id_person" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "first_name" TEXT,
    "last_name" TEXT,
    "middle_name" TEXT,
    "age" INTEGER,
    "weight" FLOAT,
    "height" INTEGER,
    "phone_number" TEXT
);

CREATE TABLE doctor (
    "id_doctor" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "first_name" TEXT,
    "last_name" TEXT,
    "middle_name" TEXT,
    "profession" TEXT,
    "phone_number" TEXT
);

CREATE TABLE pressure_data (
		"id_pressure_data" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		"date" DATE,
		"time" TIME,
		"upper_level" INTEGER,
		"lower_level" INTEGER,
		"pulse" INTEGER,
		"person_id_person" INTEGER,
		"doctor_id_doctor" INTEGER,
		FOREIGN KEY(person_id_person) REFERENCES person(id_person),
		FOREIGN KEY(doctor_id_doctor) REFERENCES doctor(id_doctor)
		);

PostgreSQL
-----------------------------

CREATE SEQUENCE id_person;
CREATE TABLE person (
		id_person INTEGER PRIMARY KEY DEFAULT NEXTVAL('id_person'),
		first_name VARCHAR(45),
		last_name VARCHAR(45),
		middle_name VARCHAR(45),
		age INTEGER,
		weight FLOAT,
		height INTEGER,
		phone_number VARCHAR(45));

CREATE SEQUENCE id_doctor;
CREATE TABLE doctor (
		id_doctor INTEGER PRIMARY KEY DEFAULT NEXTVAL('id_doctor'),
		first_name VARCHAR(45),
		last_name VARCHAR(45),
		middle_name VARCHAR(45),
		profession VARCHAR(45),
		phone_number VARCHAR(45));

CREATE SEQUENCE id_pressure_data;
CREATE TABLE pressure_data (
		id_pressure_data INTEGER PRIMARY KEY DEFAULT NEXTVAL('id_pressure_data'),
		"date" DATE,
		"time" TIME,
		upper_level INTEGER,
		lower_level INTEGER,
		pulse INTEGER,
		person_id_person INTEGER REFERENCES person(id_person),
		doctor_id_doctor INTEGER REFERENCES doctor(id_doctor)
		);