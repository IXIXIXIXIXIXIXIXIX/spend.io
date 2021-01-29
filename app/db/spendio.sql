DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS colours;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    budget NUMERIC,
    remaining_budget NUMERIC
);

CREATE TABLE colours (
    id SERIAL PRIMARY KEY,
    colourname VARCHAR(255)
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    colour_id INT REFERENCES colours(id),
    active BOOLEAN,
    reserved BOOLEAN
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN,
    default_tag INT REFERENCES tags(id)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant_id INT REFERENCES merchants(id),
    tag INT REFERENCES tags(id),
    datestamp DATE,
    amount NUMERIC
);

INSERT INTO colours(colourname) VALUES ('black');
INSERT INTO colours (colourname) VALUES ('red');
INSERT INTO colours (colourname) VALUES ('green');
INSERT INTO colours (colourname) VALUES ('blue');
INSERT INTO colours (colourname) VALUES ('purple');
