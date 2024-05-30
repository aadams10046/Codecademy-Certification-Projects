/*
Prompt: To practice what you’ve learned about window functions, you are going to use climate data from each state in the United States.
*/

SELECT * FROM state_climate LIMIT 1;


SELECT 
  state, 
  year, 
  tempf,
  AVG(tempf) OVER (PARTITION BY state ORDER BY year) as running_avg_temp
FROM state_climate;


SELECT 
  state, 
  year, 
  tempf, 
  FIRST_VALUE(tempf) OVER (PARTITION BY state ORDER BY tempf) AS 'lowest_temp' 
FROM 
  state_climate;


SELECT 
  state, 
  year, 
  tempf, 
  LAST_VALUE(tempf) OVER (PARTITION BY state ORDER BY tempf RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS 'highest_temp' 
FROM 
  state_climate;
