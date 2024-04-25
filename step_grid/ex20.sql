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
