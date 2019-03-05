DROP TABLE monday;
DROP TABLE tuesday;
DROP TABLE wednesday;
DROP TABLE thursday;
DROP TABLE friday; 
DROP TABLE users;
DROP TABLE suges;
DROP TABLE admins;

CREATE TABLE monday(
	class VARCHAR PRIMARY KEY,
	lsn1 VARCHAR,
	lsn2 VARCHAR,
	lsn3 VARCHAR,
	lsn4 VARCHAR,
	lsn5 VARCHAR,
	lsn6 VARCHAR,
	lsn7 VARCHAR,
	lsn8 VARCHAR,
	lsn9 VARCHAR,
	lsn10 VARCHAR
);

CREATE TABLE tuesday(
	class VARCHAR PRIMARY KEY,
	lsn1 VARCHAR,
	lsn2 VARCHAR,
	lsn3 VARCHAR,
	lsn4 VARCHAR,
	lsn5 VARCHAR,
	lsn6 VARCHAR,
	lsn7 VARCHAR,
	lsn8 VARCHAR,
	lsn9 VARCHAR,
	lsn10 VARCHAR
);

CREATE TABLE wednesday(
	class VARCHAR PRIMARY KEY,
	lsn1 VARCHAR,
	lsn2 VARCHAR,
	lsn3 VARCHAR,
	lsn4 VARCHAR,
	lsn5 VARCHAR,
	lsn6 VARCHAR,
	lsn7 VARCHAR,
	lsn8 VARCHAR,
	lsn9 VARCHAR,
	lsn10 VARCHAR
);

CREATE TABLE thursday(
	class VARCHAR PRIMARY KEY,
	lsn1 VARCHAR,
	lsn2 VARCHAR,
	lsn3 VARCHAR,
	lsn4 VARCHAR,
	lsn5 VARCHAR,
	lsn6 VARCHAR,
	lsn7 VARCHAR,
	lsn8 VARCHAR,
	lsn9 VARCHAR,
	lsn10 VARCHAR
);

CREATE TABLE friday(
	class VARCHAR PRIMARY KEY,
	lsn1 VARCHAR,
	lsn2 VARCHAR,
	lsn3 VARCHAR,
	lsn4 VARCHAR,
	lsn5 VARCHAR,
	lsn6 VARCHAR,
	lsn7 VARCHAR,
	lsn8 VARCHAR,
	lsn9 VARCHAR,
	lsn10 VARCHAR
);

CREATE TABLE users(
	user_id VARCHAR PRIMARY KEY,
	user_name VARCHAR
);

CREATE TABLE suges(
	user_id VARCHAR PRIMARY KEY,
	sug_text VARCHAR
);

CREATE TABLE admins(
	user_id VARCHAR PRIMARY KEY
);