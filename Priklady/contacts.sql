--
-- File generated with SQLiteStudio v3.4.4 on Sat Oct 21 17:29:38 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: contacts
CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, first_name text NOT NULL, last_name text NOT NULL, email text NOT NULL);
INSERT INTO contacts (id, first_name, last_name, email) VALUES (1, 'John', 'Doe', 'john.doe@sqlitetutorial.net');
INSERT INTO contacts (id, first_name, last_name, email) VALUES (2, 'David', 'Brown', 'david.brown@sqlitetutorial.net');
INSERT INTO contacts (id, first_name, last_name, email) VALUES (3, 'Lisa', 'Smith', 'lisa.smith@sqlitetutorial.net');

-- Index: idx_contacts_email
CREATE UNIQUE INDEX IF NOT EXISTS idx_contacts_email ON contacts (email);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
