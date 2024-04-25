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