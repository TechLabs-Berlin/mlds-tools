-- setup_data.sql
CREATE TABLE techies (
  techie_name VARCHAR(50),
  techie_id INT PRIMARY KEY,
  track VARCHAR(2),
  highest_education VARCHAR(10),
  age INT,
  returning_techie BOOLEAN
);

CREATE TABLE edyoucated_activity (
  activity_id SERIAL PRIMARY KEY,
  techie_id VARCHAR(4),
  session_date DATE,
  edyoucated_hours INT
);