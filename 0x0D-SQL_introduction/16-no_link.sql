-- lists all records of the table second_table
-- Don’t list rows without a name value
-- Results should display in the order score (high to low) -> name
SELECT score, name FROM second_table WHERE name != "" ORDER BY score DESC;