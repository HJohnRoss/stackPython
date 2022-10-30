INSERT INTO dojos (name, created_at, updated_at)
VALUES ('San Jose', NOW(), NOW()),
('Online', NOW(), NOW()),
('Bel Veiw', NOW(), NOW());

DELETE FROM dojos;

INSERT INTO dojos (name, created_at, updated_at)
VALUES ('Online', NOW(), NOW()),
('Bel Veiw', NOW(), NOW()),
('Seattle', NOW(), NOW());

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('John', 'Ross', 20, 4),
('Killian', 'Page', 25, 4),
('Uchenna', 'A.', 25, 4);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Jeffery', 'Ross', 20, 5),
('Robert', 'Page', 25, 5),
('Chandler', 'A.', 25, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Alex', 'Ross', 20, 6),
('Brian', 'Page', 25, 6),
('Austin', 'A.', 25, 6);

SELECT * FROM ninjas;

SELECT * FROM ninjas WHERE id=4;

SELECT * FROM ninjas WHERE id=6;

SELECT * FROM ninjas WHERE dojo_id=6;