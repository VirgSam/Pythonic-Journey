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