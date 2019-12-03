#DocOffice File
import pymysql

#database connection
#connection = pymysql.connect(host="localhost", user="root", passwd="", database="database")
conn = pymysql.connect(host="localhost", user="root", passwd="")

cursor = conn.cursor()
cursor.execute('DROP DATABASE IF EXISTS DocOffice')
#conn.cursor().execute('DROP DATABASE IF EXISTS DocOffice')
cursor.execute('CREATE DATABASE DocOffice')
cursor.execute('USE DocOffice')


# Queries for creating table
createDoctor = """CREATE TABLE Doctors(
  D_id            VARCHAR(6)        NOT NULL,
  Fname           VARCHAR(15)       NOT NULL,
  Lname           VARCHAR(15)       NOT NULL,
  Speciality      VARCHAR(30),
  PRIMARY KEY (D_id))"""

createPatients = """CREATE TABLE Patients(
  P_id            VARCHAR(6)        NOT NULL,
  Fname           VARCHAR(15)       NOT NULL,
  Lname           VARCHAR(15)       NOT NULL,
  Prim_Phone      VARCHAR(10)       NOT NULL,
  Pat_doc_id      VARCHAR(6)        NOT NULL,
  PRIMARY KEY (P_id),
  FOREIGN KEY (Pat_doc_id) REFERENCES Doctors(D_id))"""

createVisit = """CREATE TABLE Visits(
  P_id            VARCHAR(6)         NOT NULL, 
  D_id            VARCHAR(6)         NOT NULL,
  VisitDate       DATE               NOT NULL,
  FOREIGN KEY (P_id) REFERENCES Patients(P_id),
  FOREIGN KEY (D_id) REFERENCES Doctors(D_id))"""

createPrescriptions = """CREATE TABLE Prescriptions(
  P_id            VARCHAR(6)        NOT NULL,
  D_id            VARCHAR(6)        NOT NULL,
  Pres_name       VARCHAR(20)       NOT NULL,
  FOREIGN KEY (P_id) REFERENCES Patients(P_id),
  FOREIGN KEY (D_id) REFERENCES Doctors(D_id))"""

createTests = """CREATE TABLE Tests(
  P_id            VARCHAR(6)        NOT NULL,
  D_id            VARCHAR(6)        NOT NULL,
  Test_name       VARCHAR(20)       NOT NULL,
  FOREIGN KEY (P_id) REFERENCES Patients(P_id),
  FOREIGN KEY (D_id) REFERENCES Doctors(D_id))"""


# Creates tables in database
cursor.execute(createDoctor)
cursor.execute(createPatients)
cursor.execute(createVisit)
cursor.execute(createPrescriptions)
cursor.execute(createTests)

# Populate tables with dummy data
populateDoctors = """INSERT INTO Doctors
  VALUES
    ('RO3283', 'Rob', 'Belkin', 'Pediactrics'),
    ('AR3456', 'Alan', 'Rickman', 'Neurology'),
    ('JR2857', 'James', 'Rodgers', 'Dermatology'),
    ('TO3621', 'Tim', 'Turner', 'Radiology')"""

populatePatients = """INSERT INTO Patients
  VALUES
    ('RT3475', 'Rick', 'Toombs', '5626478976', 'AR3456'),
    ('FY2927', 'Frank', 'Young', '5622341233', 'RO3283'),
    ('JS9865', 'Juan', 'Sanchez','7144957542', 'TO3621'),
    ('KS8476', 'Kyle', 'Silver', '3235987511', 'RO3283')"""

populateVisits = """INSERT INTO Visits
  VALUES
    ('FY2927', 'RO3283', 2019-03-10),
    ('KS8476', 'RO3283', 2019-04-17),
    ('JS9865', 'TO3621', 2019-10-02),
    ('RT3475', 'AR3456', 2019-11-23)"""

populatePrescriptions = """INSERT INTO Prescriptions
  VALUES
    ('FY2927', 'RO3283', 'Percocet'),
    ('KS8476', 'RO3283', 'Albuterol'),
    ('JS9865', 'TO3621', 'Panadol'),
    ('RT3475', 'AR3456', 'Panadol')"""

cursor.execute(populateDoctors)
cursor.execute(populatePatients)
cursor.execute(populateVisits)
cursor.execute(populatePrescriptions)

conn.commit()
conn.close()