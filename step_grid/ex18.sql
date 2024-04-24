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