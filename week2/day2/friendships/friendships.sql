SELECT * FROM user;
SELECT * FROM friendships;

INSERT INTO users (first_name, last_name)
VALUES ('Amy', 'Giver'), ('Eli', 'Byers'),
('Big', 'Bird'), ('Kermit', 'The Frog'),
('Marky', 'Mark'), ('Big', 'Bird');

INSERT INTO friendships (user_id, friend_id)
VALUES (1, 2), (1, 4), (1, 6),
(2, 1), (2, 3), (2, 5),
(3, 2), (2, 5),
(4, 3),
(5, 1), (5, 6),
(6, 2), (6, 3);


SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
JOIN users as user2 ON users.id = friendships.user_id;

SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
JOIN users as user2 ON user2.id = friendships.friend_id
WHERE users.id = 7;

SELECT COUNT(friendships.id)
FROM friendships;