/*Create Users table*/
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50)
);

-- Insert users into table
INSERT INTO users(username)
VALUES
('monahan93'),
('pferrer'),
('si93onis'),
('99stroman');

/*Create Photos table*/
CREATE TABLE photos(
    id SERIAL PRIMARY KEY,
    url VARCHAR(200),
    user_id INTEGER REFERENCES users(id)
);

-- Insert photos into table
INSERT INTO photos(url,user_id)
VALUES
('http://one.jpg',4);

-- Insert multiple photos into table
INSERT INTO photos(url,user_id)
VALUES
('http://two.jpg',1),
('http://25.jpg',1),
('http://36.jpg',1),
('http://754.jpg',2),
('http://35.jpg',3),
('http://256.jpg',4);

-- Using select and where statement to identify user_id 4 photos
SELECT 
* 
FROM
photos
WHERE
user_id = 4;

-- Using complex queries to join 2 different tables
SELECT url, username FROM photos
JOIN users ON users.id = photos.user_id;

-- Testing out deletions constraints 
DROP TABLE photos;

-- Create photos table WITH Constraint ON DELETE CASCADE
CREATE TABLE photos (
id SERIAL PRIMARY KEY,
url VARCHAR(200),
user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
 
INSERT INTO photos (url, user_id)
VALUES
('http:/one.jpg', 4),
('http:/two.jpg', 1),
('http:/25.jpg', 1),
('http:/36.jpg', 1),
('http:/754.jpg', 2),
('http:/35.jpg', 3),
('http:/256.jpg', 4);

-- Testing out the constraint
DELETE FROM users WHERE id =1;
SELECT * FROM photos; 

-- Testing out deletions constraints 2
DROP TABLE photos;

-- Create photos table WITH Constraint ON DELETE SET NULL
CREATE TABLE photos (
id SERIAL PRIMARY KEY,
url VARCHAR(200),
user_id INTEGER REFERENCES users(id) ON DELETE SET NULL
);
 
INSERT INTO photos (url, user_id)
VALUES
('http:/one.jpg', 4),
('http:/754.jpg', 2),
('http:/35.jpg', 3),
('http:/256.jpg', 4);

-- Testing out deletions constraints 2
DELETE FROM users where id = 4;
SELECT * FROM photos; 

-- drop table photos
DROP TABLE photos;