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
createPerson = """CREATE TABLE Person(
    PersonID        VARCHAR(6)      NOT NULL,
    FirstName       VARCHAR(15)     NOT NULL,
    LastName        VARCHAR(15)     NOT NULL,
    StreetAddress   VARCHAR(30)     NOT NULL,
    City            VARCHAR(15)     NOT NULL,
    State           VARCHAR(15)     NOT NULL,
    ZIP             VARCHAR(5)      NOT NULL,
    PhoneNumber     VARCHAR(10)     NOT NULL,
    SSN             VARCHAR(9)      NOT NULL,
    PRIMARY KEY (PersonID))"""

createDoctor = """CREATE TABLE Doctor(
  DoctorID          VARCHAR(6)          NOT NULL,
  MedicalDegrees    VARCHAR(50)                 ,
  PersonID          VARCHAR(6)          NOT NULL,
  PRIMARY KEY (DoctorID))"""

createPatient = """CREATE TABLE Patient(
  PatientID       VARCHAR(6)        NOT NULL,
  PhoneNumber     VARCHAR(10)       NOT NULL,
  DOB             DATE              NOT NULL,
  PersonID        VARCHAR(6)        NOT NULL,
  PRIMARY KEY (PatientID),
  FOREIGN KEY (PersonID) REFERENCES Person(PersonID))"""

createPatientVisit = """CREATE TABLE PatientVisit(
  VisitID         VARCHAR(6)         NOT NULL,
  PatientID       VARCHAR(6)         NOT NULL,
  DoctorID        VARCHAR(6)         NOT NULL,
  VisitDate       DATE               NOT NULL,
  DocNote         VARCHAR(140),
  PRIMARY KEY (VisitID),
  FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
  FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID))"""

createPrescription = """CREATE TABLE Prescription(
  PrescriptionID        VARCHAR(6)        NOT NULL,
  PrescriptionName      VARCHAR(20)       NOT NULL,
  PRIMARY KEY (PrescriptionID))"""

createTest = """CREATE TABLE Test(
  TestID          VARCHAR(6)        NOT NULL,
  TestName        VARCHAR(20)       NOT NULL,
  PRIMARY KEY (TestID))"""

createPVisitTest = """CREATE TABLE PVisitTest(
    VisitID     VARCHAR(6)      NOT NULL,
    TestID      VARCHAR(6)      NOT NULL,
    FOREIGN KEY (VisitID) REFERENCES PatientVisit(VisitID),
    FOREIGN KEY (TestID) REFERENCES Test(TestID))"""

createPVisitPrescription = """CREATE TABLE PVisitPrescription(
    VisitID               VARCHAR(6)      NOT NULL,
    PrescriptionID        VARCHAR(6)      NOT NULL,
    FOREIGN KEY (VisitID) REFERENCES PatientVisit(VisitID),
    FOREIGN KEY (PrescriptionID) REFERENCES Prescription(PrescriptionID))
    """

createSpecialty = """CREATE TABLE Specialty(
    SpecialtyID     VARCHAR(6)      NOT NULL,
    SpecialtyName   VARCHAR(20)     NOT NULL,
    PRIMARY KEY (SpecialtyID))"""

createDoctorSpecialty = """CREATE TABLE DoctorSpecialty(
    DoctorID        VARCHAR(6)         NOT NULL,
    SpecialtyID     VARCHAR(6)         NOT NULL,
    FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID),
    FOREIGN KEY (SpecialtyID) REFERENCES Specialty(SpecialtyID))"""





# Creates tables in database
cursor.execute(createPerson)
cursor.execute(createDoctor)
cursor.execute(createPatient)
cursor.execute(createPatientVisit)
cursor.execute(createPrescription)
cursor.execute(createTest)
cursor.execute(createPVisitTest)
cursor.execute(createPVisitPrescription)
cursor.execute(createSpecialty)
cursor.execute(createDoctorSpecialty)


# Populate tables with dummy data
populateDoctor = """INSERT INTO Doctor
  VALUES 
    ('RB3283', 'Neurology', 'RB1234'),
    ('AR3456', 'Biology', 'AR4586'),
    ('JR2857', 'BioChemistry', 'JR3845'),
    ('TO3621', 'Organic Chemistry', 'TO9876')"""

#populateDoctor = """INSERT INTO Doctor
#  VALUES
#    ('RB3283', 'Rob', 'Belkin', 'Pediactrics'),
#    ('AR3456', 'Alan', 'Rickman', 'Neurology'),
#    ('JR2857', 'James', 'Rodgers', 'Dermatology'),
#    ('TO3621', 'Tim', 'Turner', 'Radiology')"""

populatePatient = """INSERT INTO Patient
  VALUES
    ('RT3475', 'Rick', 'Toombs', '5626478976', 'AR3456'),
    ('FY2927', 'Frank', 'Young', '5622341233', 'RO3283'),
    ('JS9865', 'Juan', 'Sanchez','7144957542', 'TO3621'),
    ('KS8476', 'Kyle', 'Silver', '3235987511', 'RO3283')"""

populateVisit = """INSERT INTO PatientVisit
  VALUES
    ('FY2927', 'RO3283', 2019-03-10),
    ('KS8476', 'RO3283', 2019-04-17),
    ('JS9865', 'TO3621', 2019-10-02),
    ('RT3475', 'AR3456', 2019-11-23)"""

populatePrescription = """INSERT INTO Prescriptions
  VALUES
    ('FY2927', 'RO3283', 'Percocet'),
    ('KS8476', 'RO3283', 'Albuterol'),
    ('JS9865', 'TO3621', 'Panadol'),
    ('RT3475', 'AR3456', 'Panadol')"""

cursor.execute(populateDoctor)
#cursor.execute(populatePatient)
#cursor.execute(populateVisit)
#cursor.execute(populatePrescription)

conn.commit()
conn.close()