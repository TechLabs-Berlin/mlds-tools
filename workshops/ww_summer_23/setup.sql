-- setup.sql
CREATE TABLE techies (
  techie_name VARCHAR(50),
  techie_id INT PRIMARY KEY,
  track VARCHAR(2),
  highest_education VARCHAR(15),
  age INT,
  returning_techie BOOLEAN
);

CREATE TABLE edyoucated_activity (
  techie_id VARCHAR(4),
  session_date DATE,
  edyoucated_hours INT
);

COPY techies from '/tmp/techies.csv' DELIMITER ',' CSV HEADER;
COPY edyoucated_activity from '/tmp/edyoucated.csv' DELIMITER ',' CSV HEADER;