CREATE TABLE users(
	id SERIAL PRIMARY KEY,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	username VARCHAR(30) NOT NULL,
	bio VARCHAR(400),
	avatar VARCHAR(200),
	phone VARCHAR(25),
	email VARCHAR(45),
	password VARCHAR(50),
	status VARCHAR(15),
	CHECK(COALESCE(phone,email)IS NOT NULL),
		
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    url VARCHAR(200) NOT NULL,
    caption VARCHAR(240),
    lat REAL CHECK( lat IS NULL OR (lat >= -90 AND lat <= 90)),
    lng REAL CHECK( lat IS NULL OR (lat >= -180 AND lat <= 180)),
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE

);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    contents VARCHAR(240) NOT NULL,
    caption VARCHAR(240),
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
	post_id INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE

);

CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    post_id INTEGER REFERENCES posts(id) ON DELETE CASCADE,
    comment_id INTEGER REFERENCES comments(id) ON DELETE CASCADE,
    CHECK (
		COALESCE ((post_id)::BOOLEAN::INTEGER, 0)
		+
		COALESCE ((comment_id)::BOOLEAN::INTEGER, 0)
		= 1
	),
	UNIQUE(user_id,post_id,comment_id)
	
);

CREATE TABLE photo_tags (
    id SERIAL PRIMARY KEY,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    post_id INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    x INTEGER NOT NULL,
	y INTEGER NOT NULL,
	UNIQUE(user_id,post_id)
);

CREATE TABLE caption_tags (
    id SERIAL PRIMARY KEY,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    post_id INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
	UNIQUE(user_id,post_id)
);

CREATE TABLE hashtags (
    id SERIAL PRIMARY KEY,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	title VARCHAR(20) NOT NULL UNIQUE
	
);

CREATE TABLE hashtags_posts (
    id SERIAL PRIMARY KEY,
	hashtag_id INTEGER NOT NULL REFERENCES hashtags(id) ON DELETE CASCADE,
	post_id INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
	UNIQUE(hashtag_id,post_id)
	
);

CREATE TABLE followers (
    id SERIAL PRIMARY KEY,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	leader_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
	follower_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
	UNIQUE(leader_id,follower_id)	
);

-- Practice query
/* Join the users and post table
   Show the username of use id 200 and the
   captions of all related posts
   they have
*/
SELECT username,caption
FROM users
JOIN posts ON posts.user_id = users.id
WHERE posts.user_id = 200;

--  Practice query
/* Show each username and the number
   of likes that they have created.
*/
SELECT username, count(*)
FROM users
JOIN likes ON likes.user_id = users.id
GROUP BY username;

-- Understanding where Postgres stores data
SHOW data_directory;

-- Show current databases created and internal identifier for each
SELECT oid,datname
FROM pg_database;

-- Show classes and individual objects in db
SELECT *
FROM pg_class;

-- How to create an index on Table user(username) to speed up query retrieval
CREATE INDEX ON users (username);

-- How do delete an index
DROP INDEX users_username_idx;

-- Benchmarking Queries
SELECT *
FROM users
WHERE username = 'Emil30';

-- With an index it took about 0.130 ms
-- Second part of benchmarking
EXPLAIN ANALYZE SELECT *
FROM users
WHERE username = 'Emil30';

-- Third part of benchmarking
-- Without an index it took about 2.057 ms

DROP INDEX users_username_idx;
EXPLAIN ANALYZE SELECT *
FROM users
WHERE username = 'Emil30';

-- Downsides of Indexes, comes with storage capacity limitation and slowing down update speed
CREATE INDEX ON users (username);
SELECT pg_size_pretty(pg_relation_size('users')); -- uses 872kb
SELECT pg_size_pretty(pg_relation_size('users_username_idx')); -- 184kb

-- Automatically created indexes on Primary keys and unique contraints by postgres
SELECT relname, relkind
FROM pg_class
WHERE relkind = 'i';

-- Query tuning
-- Part 1
SELECT username,contents
FROM users
JOIN comments ON comments.user_id = users.id
WHERE username = 'Alyson14';

-- Part 2 review query plan and planning and execution times
EXPLAIN ANALYZE SELECT username,contents
FROM users
JOIN comments ON comments.user_id = users.id
WHERE username = 'Alyson14';