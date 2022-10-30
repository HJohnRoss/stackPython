SELECT * FROM users;
SELECT * FROM books;
SELECT * FROM users_has_books;

INSERT INTO users (first_name, last_name)
VALUES ('Jane', 'Amsden'),
('Emily', 'Dixon'),
('Theodore', 'Dostoevsky'),
('William', 'Shapiro'),
('Lao', 'Xiu');

INSERT INTO books (title, num_of_pages)
VALUES ('C Sharp', 567),
('Java', 1096),
('Python', 703),
('PHP', 1102),
('Ruby', 692);

UPDATE books_schema_db.books SET
title = 'C#'
WHERE id=1;

UPDATE books_schema_db.users SET
first_name = 'Bill'
WHERE id=4;

INSERT INTO users_has_books (users_id, books_id)
VALUES (1,1);

INSERT INTO users_has_books (users_id, books_id)
VALUES (2, 1), (2, 2), (2, 3), 
(3, 1), (3, 2), (3, 3), (3, 4), 
(4, 1), (4, 2), (4, 3), (4, 4), (4, 5);

SELECT * FROM users
JOIN users_has_books ON users.id = users_has_books.users_id
WHERE users_has_books.books_id = 3;

DELETE FROM users_has_books WHERE users_id = 2;

INSERT INTO users_has_books (users_id, books_id)
VALUES (5, 2);

SELECT * FROM books
JOIN users_has_books ON books.id = users_has_books.books_id
WHERE users_has_books.users_id = 3;

SELECT * FROM users
JOIN users_has_books ON users.id = users_has_books.users_id
WHERE users_has_books.books_id = 5;