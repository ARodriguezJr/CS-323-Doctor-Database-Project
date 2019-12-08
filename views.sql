
/* Number 1: Previous Script written */



/* Number 2:  Doctor Rob Belkin is retiring. We need to inform all his patients, and ask them to
select a new doctor. For this purpose, Create a VIEW that finds the names and
Phone numbers of all of Rob's patients.
*/
CREATE VIEW Rob_Patient
AS
SELECT p.FirstName, p.LastName, p.PhoneNumber
FROM Person AS p
INNER Join Patient AS pt
ON pt.PersonID = p.PersonID

INNER JOIN PatientVisit pv
ON pv.PatientID = pt.PatientID
WHERE pv.DoctorID IN (SELECT d.DoctorID FROM Doctor AS d
                        INNER JOIN Person AS pr ON pr.PersonID = d.PersonID
                        WHERE pr.FirstName = "ROB" AND pr.LastName = "BELKIN")



/* Number 3: Create a view which has First Names, Last Names of all doctors who gave out
prescription for Panadol.
*/
CREATE VIEW Pandol_Doctor
AS
SELECT p.FirstName, pLastName
From Person AS p
INNER JOIN Doctor AS d
ON p.PersonID = d.DoctorID
INNER JOIN PatientVisit AS pv
ON pv.DoctorID = d.DoctorID
INNER JOIN PVisitPrescription AS pp
ON pv.VisitID = pp.VisitID
INNER JOIN Prescription AS pr
ON pr.PrescriptionID = pp.PrescriptionID
WHERE pr.PrescriptionName = "Pandol";




/* Number 4: Create a view which shows the First Name and Last name of all doctors and their
specialty’s.
*/

CREATE VIEW Doctor_Specialities
AS
SELECT 


/*Number 5: Modify the view created in Q4 to show the First Name and Last name of all
doctors and their specialties ALSO include doctors who DO NOT have any
specialty. */




/*Number 6: Create trigger on the DoctorSpecialty so that every time a doctor
            specialty is updated or added, a new entry is made in the audit table.
*/
CREATE or REPLACE TRIGGER Audit_change
AFTER
UPDATE[of Audit]
ON DoctorSpecialty
BEGIN
    INSERT INTO Audit VALUES ('Doctor specialty is updated', sysdate);
END;

CREATE TRIGGER update_audit
AFTER UPDATE ON DoctorSpecialty
FOR EACH ROW
BEGIN
    INSERT INTO sp_audit
    DoctorID = OLD.DoctorID,
    SpecialtyID = OLD.SpecialtyID;
END;

/* Number 7:  Create a script to do the following (Write the script for this)
                    a. If first time backup take backup of all the tables
                    b. If not the first time remove the previous backup tables and take new
                        backups.

*/





/* Extra Credit:
*/
 