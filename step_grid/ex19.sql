/*You are building a database of a naval shipping company, you need to store a list of boats and the crew members who work on eachm, so create a table called boats and a table 
called crew_members. From the perspective of the boat, this is a one-many relationship.
To complete the design, you need to do two things:
1. Add a column to the crew_members table definition that will relate crew_members to boats. You should call this foreign key column boat_id.
2. Write a query the will fetch all crew_members associated with the boat that has an ID of 1.*/

-- create table called boats
CREATE TABLE boats(
    id SERIAL PRIMARY KEY,
    name VARCHAR(200)
);



-- insert 2 boats
INSERT INTO boats(name)
VALUES
('Rogue Wave'),
('Harbor Master');


-- create table called 'crew_members'
CREATE TABLE crew_members(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    boat_id INTEGER REFERENCES boats(id)
);

-- insert 3 crew members
INSERT INTO crew_members (first_name,boat_id)
VALUES
('Alex',1),
('Lucia',1),
('Ari',2);

-- Write a query that will fetch all crew_members with Boat id 1
SELECT * FROM crew_members
WHERE 
boat_id = 1;