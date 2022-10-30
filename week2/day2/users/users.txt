INSERT INTO users (first_name, last_name, email, created_at, updated_at)
VALUES ('John', 'Ross', 'rossjohn936@gmail.com', NOW(), NOW()),
('Uchenna', 'A.', 'uchenna@codingdojo.com', NOW(), NOW()),
('Mark', 'Ubiadas', 'mark@codingdojo.com', NOW(), NOW());

SELECT first_name, last_name FROM users;

SELECT email FROM users WHERE id = 1;

SELECT email FROM users ORDER BY id DESC LIMIT 1;

UPDATE users
SET last_name = 'Pancakes'
WHERE id = 3;

DELETE FROM users WHERE id = 2;

SELECT * FROM users ORDER BY first_name

SELECT * FROM users ORDER BY first_name DESC;