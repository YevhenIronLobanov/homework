SELECT JOB_ID, Count(EMPLOYEE_ID) AS Count_employee FROM employees
GROUP BY JOB_ID;