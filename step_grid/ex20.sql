/*Practice Joining Data
You are designing a database for a book publishing company.  
The database needs to store a table of authors and books. An author has many books.  
This means that books should have a foreign key column that references an author.
Write a query that will join together these two tables.  For each book, print the title of the book and the name of the author.*/

-- Create table authors
CREATE TABLE authors(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

-- Create table books
CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author_id INTEGER REFERENCES authors(id) ON DELETE CASCADE
);

-- Insert into authors table
INSERT INTO authors(name)
VALUES
('JK Rowling '),
('Stephen King '),
('Agatha Christie'),
('Dr Seuss ');

-- Insert into books table
INSERT INTO books(title,author_id)
VALUES
('It',2),
('Chamber of Secrets',1),
('Cat and the Hat',4),
('Affair at Styles',3);

-- Query to join tables and print title of book and name of author
SELECT title,name 
FROM authors
JOIN books on books.author_id = authors.id;

-- perform full outer join on authors and books
SELECT title, name 
FROM books
FULL JOIN authors ON books.author_id = authors.id;

/*Three way join exercise
Write a query that will return the title of each book, 
along with the name of the author, and the rating of a review.  
Only show rows where the author of the book is also the author of the review.  */

-- Delete table books
DROP TABLE books;

-- Create table books
CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author_id INTEGER REFERENCES authors(id) ON DELETE CASCADE
);

-- Insert new values into table books
INSERT INTO books(title,author_id)
VALUES
('The Dark Tower',1),
('Affair At Stylest',2),
('Chamber of Secrets',3);

-- Create table reviews
CREATE TABLE reviews(
    id SERIAL PRIMARY KEY,
    ratings INTEGER,
    reviewer_id INTEGER,
    book_id INTEGER REFERENCES books(id) ON DELETE CASCADE
);

-- Insert new values into table reviews
INSERT INTO reviews(ratings,reviewer_id,book_id)
VALUES
(3,1,2),
(4,2,1),
(5,3,3);

-- Perform three way join
SELECT title, name, ratings
FROM reviews
JOIN books ON books.id = reviews.book_id
JOIN authors ON author_id = books.author_id and authors.id = reviews.reviewer_id;