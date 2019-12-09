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
  DoctorID              VARCHAR(6)          NOT NULL,
  MedicalDegrees    VARCHAR(50)                 ,
  PersonID          VARCHAR(6)          NOT NULL,
  PRIMARY KEY (D_id))"""

createPatient = """CREATE TABLE Patient(
  PatientID       VARCHAR(6)        NOT NULL,
  PhoneNumber     VARCHAR(10)       NOT NULL,
  DOB             DATE              NOT NULL,
  PersonID        VARCHAR(6)        NOT NULL,
  PRIMARY KEY (P_id),
  FOREIGN KEY (PersonID) REFERENCES Person(PersonID))"""

createPatientVisit = """CREATE TABLE Visits(
  VisitID         VARCHAR(6)         NOT NULL,
  PatientID       VARCHAR(6)         NOT NULL,
  DoctorID        VARCHAR(6)         NOT NULL,
  VisitDate       DATE               NOT NULL,
  DocNote         VARCHAR(140),
  PRIMARY KEY (VisitID),
  FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
  FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID))"""

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

createDoctorSpecialty = """CREATE TABLE DoctorSpecialty(
    DoctorID        VARCHAR(6)         NOT NULL,
    SpecialtyID     VARCHAR(6)         NOT NULL,
    FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID),
    FOREIGN KEY (SpecialtyID) REFERENCES Specialty(SpecialtyID))"""

createSpecialty = """CREATE TABLE Specialty(
    SpecialtyID     VARCHAR(6)      NOT NULL,
    SpecialtyName   VARCHAR(20)     NOT NULL,
    PRIMARY KEY (SpecialtyID))"""

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



# Creates tables in database
cursor.execute(createDoctor)
cursor.execute(createPatient)
cursor.execute(createPatientVisit)
cursor.execute(createPrescription)
cursor.execute(createTest)
cursor.execute(createPatientVisit)
cursor.execute(createDoctorSpecialty)
cursor.execute(createSpecialty)
cursor.execute(createPVisitPrescription)
cursor.execute(createPerson)

# Populate tables with dummy data
populateDoctor = """INSERT INTO Doctors
  VALUES
    ('RO3283', 'Pediactrics', '3283'),
    ('AL3456', 'Neurology', '3456')"""

populatePatient = """INSERT INTO Patient
  VALUES
    ('J67L', '5626478976', 1959-03-10, '1234'),
    ('D33M', '3235987511', 1929-09-10, '4567')"""

populatePatientVisit = """INSERT INTO Visits
  VALUES
    ('0000', 'J67L', 'RO3283', 2019-04-12, 'In great condition'),
    ('3333', 'D33M', 'AL3456', 2019-04-20, 'Great')"""

populatePrescription = """INSERT INTO Prescription
  VALUES
    ('Rad', 'Strong'),
    ('Alt', 'Weak')"""

populateTest = """INSERT INTO Test
  VALUES
    ('A12', 'Rad'),
    ('K27', 'Alt')"""

populatePVisitTest = """INSERT INTO PVisitPrescription
  VALUES
    ('0000', 'A12'),
    ('3333', 'K27')"""

populatePVisitPrescription = """INSERT INTO PVisitPrescription
  VALUES
    ('0000', 'Rad'),
    ('3333', 'Alt')"""

populateDoctorSpecialty = """INSERT INTO DoctorSpecialty
  VALUES
    ('RO3283', 'EYES'),
    ('AL3456', 'MOUTH')"""

populateSpecialty = """INSERT INTO Specialty
  VALUES
    ('EYES', 'Retina'),
    ('MOUTH', 'Teeth')"""

populatePerson = """INSERT INTO Person
  VALUES
    ('3283', 'Robert', 'Belkin', '800 State College', 'Fullerton', '90643', '4567345678', '328332830'),
    ('3456', 'Alan', 'Rickman', '410 El Rancho', 'La Habra', '90631', '6264567007', '123456789'),
    ('1234', 'Robert', 'Morris', '320 Shady Lane', 'Yorba Linda', '90123', '5626478976', '234567890'),
    ('4567', 'Martin', 'Rodriguez', '540 Painter Ave', 'Whittier', '90893', '3235987511', '345678901')"""

cursor.execute(populateDoctor)
cursor.execute(populatePatient)
cursor.execute(populatePatientVisit)
cursor.execute(populatePrescription)
cursor.execute(populateTest)
cursor.execute(populatePatientVisit)
cursor.execute(populateDoctorSpecialty)
cursor.execute(populateSpecialty)
cursor.execute(populatePVisitPrescription)
cursor.execute(populatePerson)




conn.commit()
conn.close()