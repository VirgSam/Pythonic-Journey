CREATE TABLE users(
	id SERIAL PRIMARY KEY,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	username VARCHAR(30) NOT NULL,
	bio VARCHAR(400),
	avatar VARCHAR(200),
	phone VARCHAR(25),
	email VARCHAR(25),
	password VARCHAR(50),
	status VARCHAR(15),
	CHECK(COALESCE(phone,email)IS NOT NULL),
	CHECK(COALESCE(email,password)IS NOT NULL)
	
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