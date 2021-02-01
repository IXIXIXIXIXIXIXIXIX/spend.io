DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS colours;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    budget NUMERIC(12, 2),
    remaining_budget NUMERIC(12, 2)
);

CREATE TABLE colours (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
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
    default_tag_id INT REFERENCES tags(id)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant_id INT REFERENCES merchants(id),
    tag_id INT REFERENCES tags(id),
    datestamp DATE,
    amount NUMERIC(12,2)
);

INSERT INTO users (name, budget, remaining_budget) VALUES ('Scott', 2000.00, 2000.00);

